# Kafka_Producer_for_ToIot
ToIot의 Kafka로 임시 데이터를 보내는 프로그램. 

Installation
=======
```sh
$ git clone https://github.com/ksh24865/Kafka_Producer_for_ToIot.git
```
```sh
$ pip3 install kafka-python
```

Run
=======
```sh
$ python3 run.py
```

Information
=======
* Sensor
  |name|id|values|
  |----|--|------|
  |air-dust|6|ultrafine-dust, fine-dust|
  |air-temp|7|temperature, relative-humidity|
  |air-noise|8|noise|

* node
  |sink|name|id|sensors|
  |----|----|--|------|
  |2|영등포구|2~61|air-dust, air-temp, air-noise|
  |3|관악구|62~121|air-dust, air-temp, air-noise|
  |4|동작구|122~181|air-dust, air-temp, air-noise|
  |5|서초구|182~241|air-dust, air-temp, air-noise|
  |6|강남구|242~301|air-dust, air-temp, air-noise|
  |7|송파구|302~362|air-dust, air-temp, air-noise|
  
