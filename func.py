from kafka import KafkaProducer 
from json import dumps 
from datetime import datetime
import time 
import conf
# node : 2~362
# sensor : 6(초미먼,미먼), 7(온도,습도), 8(소음)

def put_air_dust(producer,node,time):
    data = {"sensor_id":6,"node_id":node,"values":[1,2],"timestamp":time}
    producer.send('sensor-data', value=data) 
    producer.flush() 
def put_air_noise(producer,node,time):
    data = {"sensor_id":8,"node_id":node,"values":[1],"timestamp":time}
    producer.send('sensor-data', value=data) 
    producer.flush() 
def put_air_temp(producer,node,time):
    data = {"sensor_id":7,"node_id":node,"values":[1,2],"timestamp":time}
    producer.send('sensor-data', value=data) 
    producer.flush() 
def now():
    return str(datetime.fromtimestamp(time.time()))[:19]
def put_data():
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=[conf.ip + ':' + conf.port], value_serializer=lambda x: dumps(x).encode('utf-8')) 
    time = now()
    for node in range(2,363):
        put_air_dust(producer,node,time)
        put_air_noise(producer,node,time)
        put_air_temp(producer,node,time)
def put_data_simple():
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=[conf.ip + ':' + conf.port], value_serializer=lambda x: dumps(x).encode('utf-8')) 
    time = now()
    for node in range(2,363):
        for sensor in range(6,9):
            if sensor == 8:
                data = {"sensor_id":sensor,"node_id":node,"values":[1],"timestamp":time}
            else:
                data = {"sensor_id":sensor,"node_id":node,"values":[1,2],"timestamp":time}
            producer.send('sensor-data', value=data) 
            producer.flush() 


#print("elapsed :", time.time() - start)
