from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    bootstrap_servers=f'kafka-3b883d25-ronenb75-0acd.aivencloud.com:19777',
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    value_deserializer = lambda v: json.loads(v.decode('ascii'))
)

consumer.subscribe(topics='Out01')
for message in consumer:
  print ("%d:%d: v=%s" % (message.partition,
                          message.offset,
                          message.value))