#!/usr/bin/python
import serial
ser = serial.Serial('/dev/ttyS0',115200)
while True:
    readedText = ser.readline()
    print(readedText.decode("utf-8"), end='')
ser.close()
