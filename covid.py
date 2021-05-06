import requests
import json
import os
import time

url='https://cdn-api.co-vin.in//api/v2/appointment/sessions/public/calendarByDistrict?district_id=366&date=06-05-2021'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', 'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Origin': 'https://www.cowin.gov.in','Referer': 'https://www.cowin.gov.in/'}
unavailable=True
while(unavailable):
    req=requests.get(url,headers=header)
    x=json.loads(req.text)
    for i in x['centers']:
        for j in i['sessions']:
            if (j['available_capacity']>0):
                print(i['name'],j['available_capacity'])
                unavailable=False
                os.startfile('E:\\MUSIC\\RISE I Worlds 2018 - League of Legends.mp3')
                break
    time.sleep(2)
    print('running....')
    
