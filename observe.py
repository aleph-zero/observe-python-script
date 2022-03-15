#!/usr/bin/env python3

import json
import time
import requests
import datetime

OBSERVE_CUSTOMER_ID="<OBSERVE_CUSTOMER_ID>"
OBSERVE_INGEST_TOKEN="<OBSERVE_INGEST_TOKEN>"
OBSERVE_URL="https://collect.observeinc.com/v1/http/?ts={}"

sleep_time_seconds = 30

def main():

    while True:      
        data = my_awesome_function_to_grab_data_from_somewhere() // CHANGE THIS
        observe(data)
        time.sleep(sleep_time_seconds)

def observe(payload):

    auth = 'Bearer {} {}'.format(OBSERVE_CUSTOMER_ID, OBSERVE_INGEST_TOKEN)

    ts = datetime.datetime.now()
    url = OBSERVE_URL.format(ts)

    headers = { 
            'Content-type'  : 'application/json',
            'Authorization' : auth
            }

    response = requests.post(url, json=payload, headers=headers)
    return

if __name__=="__main__":
    main()
