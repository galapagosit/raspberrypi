
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

try:
    while True:
        GPIO.output(25, GPIO.HIGH)
        sleep(0.001)
        GPIO.output(25, GPIO.LOW)
        sleep(0.01)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
