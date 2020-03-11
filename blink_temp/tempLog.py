#Use the temp funtion every 60 seconds
import os
import time
import Adafruit_DHT
import sqlite3 as sql 
import smtplib

#Assign GPIO pins
tempPin = 6

#Temp and Humidity sensor
tempSensor = Adafruit_DHT.DHT11

con = sql.connect('tempLog.db')
cur = con.cursor()

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor,tempPin)
	temperature = temperature * 9/5.0 + 32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}'.format(temperature)
		humid = '{1:0.1f}'.format(temperature, humidity)
		print(tempFahr, humid)
	else:
		print('Error reading sensor.')

	return tempFahr, humid
try:
	while True:
		dataT, dataH  = readF (tempPin)
		cur.execute('INSERT INTO tempLog VALUES(?,?,?)',(time.strftime('%Y-%m-%d %H:%M:%S'),dataT, dataH))
		con.commit()
		table = con.execute("select * from tempLog")
		time.sleep(5)

except KeyboardInterrupt:
	os.system('clear')
	con.close()
	exit(0)
