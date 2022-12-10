#!/usr/bin/python
import serial
import datetime
ser = serial.Serial('/dev/ttyS0',115200)

logfile = open("esp32-logs.txt", 'a')
while True:
    try:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        readedText = ser.readline()
        byte_line = readedText.decode("utf-8")

        line_to_save = f"{current_time}:  {byte_line}"

        print(line_to_save, end='')
        logfile.write(line_to_save)
    except Exception:
        print("Unable to read serial")

ser.close()
