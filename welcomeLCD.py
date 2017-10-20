#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

lcd.clear()
lcd.message('   Welcome To\n')
lcd.message("Cooper's  Feeder")
sleep(3)
lcd.clear()
lcd.message('      MEOW\n')
lcd.message("   MEOW  MEOW")
sleep(3)
lcd.clear()

