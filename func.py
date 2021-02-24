from kafka import KafkaProducer 
from json import dumps 
from datetime import datetime
import time 
import conf


def put_air_dust(producer,node,time):
    data = {"sensor_id":3,"node_id":node,"values":[1,2],"timestamp":time}
    producer.send(conf.topicName, value=data) 
    producer.flush() 
def put_air_noise(producer,node,time):
    data = {"sensor_id":4,"node_id":node,"values":[1],"timestamp":time}
    producer.send(conf.topicName, value=data) 
    producer.flush() 
def put_air_temp(producer,node,time):
    data = {"sensor_id":5,"node_id":node,"values":[1,2],"timestamp":time}
    producer.send(conf.topicName, value=data) 
    producer.flush() 
def now():
    return str(datetime.fromtimestamp(time.time()))[:19]
def put_data():
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=[conf.ip + ':' + conf.port], value_serializer=lambda x: dumps(x).encode('utf-8')) 
    time = now()
    for node in conf.nodes:
        put_air_dust(producer,node,time)
        put_air_noise(producer,node,time)
        put_air_temp(producer,node,time)
def put_data_simple():
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=[conf.ip + ':' + conf.port], value_serializer=lambda x: dumps(x).encode('utf-8')) 
    time = now()
    for node in conf.nodes:
        for sensor in conf.sensors:
            if sensor == 9:
                data = {"sensor_id":sensor,"node_id":node,"values":[1],"timestamp":time}
            else:
                data = {"sensor_id":sensor,"node_id":node,"values":[1,2],"timestamp":time}
            producer.send('sensor-data', value=data) 
            producer.flush() 


#print("elapsed :", time.time() - start)
