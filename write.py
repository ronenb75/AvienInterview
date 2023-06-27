import time
from datetime import datetime
import json
import uuid
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=f'kafka-3b883d25-ronenb75-0acd.aivencloud.com:19777',
    security_protocol="SSL",
    ssl_cafile="./ca.pem",
    ssl_certfile="./service.cert",
    ssl_keyfile="./service.key",
 #value_serializer=lambda v: json.dumps(v).encode('ascii')
)

trucks = [
    {"id": 1, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 2, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 3, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 4, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 5, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 6, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 7, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 8, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 9, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
    {"id": 10, "batt": 100, "frontPreesure": 50, "backPressure": 52, "speed": 0},
]

while True:
    for truck in trucks:
        truck['batt'] += random.randint(-10,2)/10
        if truck['batt'] > 100:
            truck['batt'] = 100

        truck['frontPreesure'] += (random.random() - 0.5)/100
        truck['backPressure'] += (random.random() - 0.5)/100
        truck['speed'] += random.randint(-10 , 10)
        if truck['speed'] < 0:
            truck['speed'] = 0
    
        key = {
            "uuid": str(uuid.uuid4())
        }


        message = {
            "timeS": datetime.now().isoformat(),
            "truckID": truck['id'],
            "batt": truck['batt'],
            "frontPreesure": truck['frontPreesure'],
            "backPressure": truck['backPressure'],
            "speed": truck['speed'],
        }

        #print(key)
        #print(message)

        producer.send('In', key=json.dumps(key).encode('ascii'), value=json.dumps(message).encode('ascii'))
        producer.flush()
        print(f"Truck {truck['id']} sent...")
        time.sleep(1)