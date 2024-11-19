import requests

def go():
    r = requests.get('http://192.168.1.111/v1/current_conditions')
    if(r.status_code == 200):
        r = r.json()
        r = r['data']
        print(r['ts'])



if __name__ == '__main__':
    go()




