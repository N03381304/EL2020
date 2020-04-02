#Import Libraries we will be using
import Adafruit_DHT 
import os

#Assign GPIO pins
tempPin = 6

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11

while True: 
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 + 32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}'.format(temperature)
		print('Temperature = {0:0.1f}  Humidity = {1:0.1f}'.format(temperature, humidity))
	else:
		print('Failed to get reading. Try again!')

