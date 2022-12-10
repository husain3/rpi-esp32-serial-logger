#!/usr/bin/python
import serial
import datetime
ser = serial.Serial('/dev/ttyS0',115200)
while True:
    try:
        readedText = ser.readline()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        byte_line = readedText.decode("utf-8")
        print(f"{current_time}:  {byte_line}", end='')
    except Exception:
        print("Unable to read serial")
ser.close()
