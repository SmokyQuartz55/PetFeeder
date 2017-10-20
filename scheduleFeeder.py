from time import sleep
import RPi.GPIO as GPIO
import time
import atexit
import schedule

DIR = 20 #Directtion GPIO Pin
STEP = 16 #Step GPIO Pin
CW = 1 #Clockwise Direction
CCW = 0 #Counter clockwise Rotation
SPR = 66 #Stepts per Rotation (360/1.8)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)

#MODE = (14,15,18) #Microstep Resolution Pins
#GPIO.setup(MODE, GPIO.OUT)
#RESOLUTION = {'Full': (0, 0, 0),
#              'Half': (1, 0, 0),
#              '1/4': (0, 1, 0),
#              '1/8': (1, 1, 0),
#              '1/16': (0, 0, 1),
#              '1/32': (1, 0, 1)}
#GPIO.output(MODE, RESOLUTION['Half'])

step_count = SPR #SPR because its one full roation (times by resolution)
delay = .005 #1 second divided by Step_count (divide bu resolution 


def Morning():
    print("Good Morning")
    for i in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

def Evening():
    print("Dinner Time")
    for i in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
#def fanOn():
 #   GPIO.output(6, GPIO.LOW)
 #   time.sleep(120)
def feedOn():
    GPIO.output(6, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
def feedOff():
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)


schedule.every().day.at("6:14").do(feedOn)
schedule.every().day.at("6:15").do(Morning)
schedule.every().day.at("6:16").do(feedOff)
schedule.every().day.at("18:14").do(feedOn)
schedule.every().day.at("18:15").do(Evening)
schedule.every().day.at("18:16").do(feedOff)

GPIO.output(DIR, CW)

while True:
    schedule.run_pending()
    time.sleep(0)
    input_CCW = GPIO.input(18)
    input_CW = GPIO.input(27)
    if input_CCW == False:
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(DIR, CCW)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        GPIO.output(5, 1)
        GPIO.output(6, 1)
    elif input_CW == False:
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(DIR, CW)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        GPIO.output(5, 1)
        GPIO.output(6, 1)

