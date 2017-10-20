#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
import time
from time import sleep, strftime
from datetime import datetime
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lcd = Adafruit_CharLCD()
lcd.begin(16, 1)
lcd.message("    COOPER'S\n")
lcd.message("   Pet Feeder")
while True:
	input_stateForward = GPIO.input(13)
	input_stateReverse = GPIO.input(19)
	if input_stateForward == False:
		lcd.clear()
		lcd.message('  Forward Turn\n')
		time.sleep(1)
		lcd.clear()
 	elif input_stateReverse == False:
		lcd.clear()
		lcd.message('  Reverse Turn\n')
		time.sleep(1)
		lcd.clear()
	else:
		lcd.message("    COOPER'S\n")
		lcd.message("   Pet Feeder")
