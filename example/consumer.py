from ensurepip import bootstrap
from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer(
        'registered_user',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest', # earliest means that the consumer will read from the beginning of the topic
        group_id='consumer-group-b'
    )
    
    print('Waiting for messages...')
    for message in consumer:
        print(f'Registered user: {json.loads(message.value)}')