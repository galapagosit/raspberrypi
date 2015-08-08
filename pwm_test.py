import random
import RPi.GPIO as GPIO
from time import sleep


dc_range_up = 1
dc_range_down = 1

def my_callback(channel):
    global dc_range_up
    global dc_range_down
    if channel == 24:
        print('switch range!!')
        dc_range_up = random.randint(1, 20)
        dc_range_down = random.randint(1, 20)


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback, bouncetime=200)

p = GPIO.PWM(25, 50)
p.start(0)

try:
    while True:
        for dc in range(0, 101, dc_range_up):
            p.ChangeDutyCycle(dc)
            sleep(0.1)
        for dc in range(100, -1, -dc_range_down):
            p.ChangeDutyCycle(dc)
            sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
