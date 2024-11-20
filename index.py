import requests
import os
import sqlite3
import time

delay = 60

def go():
    db = sqlite3.connect("/data/weather.db")
    db.execute("""
        CREATE TABLE IF NOT EXISTS obs 
            (
               ts INTEGER PRIMARY KEY, 
               temp REAL,
               hum REAL,
               dew_point REAL,
               wind_speed REAL,
               wind_dir INT,
               rain_size REAL
            )
    """)
    while True:
        cur = db.cursor()
        sql = ''' INSERT INTO obs(ts, temp, hum, dew_point, wind_speed, wind_dir, rain_size)
              VALUES(?,?,?,?,?,?,?)
        '''
        r = requests.get('http://192.168.1.111/v1/current_conditions')
        if(r.status_code == 200):
            r = r.json()
            r = r['data']
            print(r['ts'])
            cur.execute(sql, (
                r['ts'],
                r['conditions'][0]['temp'],
                r['conditions'][0]['hum'],
                r['conditions'][0]['dew_point'],
                r['conditions'][0]['wind_speed_last'],
                r['conditions'][0]['wind_dir_last'],
                r['conditions'][0]['rain_size']
            ))
            db.commit()
            
        time.sleep(delay)

if __name__ == '__main__':
    go()




