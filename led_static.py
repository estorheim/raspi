# Simple script which activates +3.3 V at pin 7.

import RPi.GPIO as gpio
import time

def blink(pin):
    gpio.output(pin,gpio.HIGH)
    time.sleep(1)
    gpio.output(pin,gpio.LOW)
    time.sleep(1)
    return

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)

for i in range(0,50):
    blink(7)

gpio.cleanup()
