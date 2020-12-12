#!/usr/bin/env python3
import time
import psutil
import os
import paho.mqtt.publish as publish
from time import sleep
from uptime import uptime
f = open("/sys/class/thermal/thermal_zone4/temp")
t = f.read()
f.close()
temp=(int(t)/1000.0)
def uptimee():
    hours = int(((now - int(psutil.boot_time()))/60)/60)
    if hours < 24:
        return str(hours)
def publish_message(topic, message):
    print("mqtt topickki: " + topic)
    print("viesti: " + message)
    publish.single(topic, message, hostname="192.168.1.4")
juuri = psutil.disk_usage('/')
juuri = (int(juuri.free / (2**30)))
data = psutil.disk_usage('/data')
data = (int(data.free / (2**30)))
now = int(time.time())
publish_message("deltsu/temp",str(temp))
publish_message("deltsu/uptime", str(uptimee()))
publish_message("deltsu/juuri", str(juuri))
publish_message("deltsu/data", str(data))
