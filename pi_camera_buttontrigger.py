# Make take a picture with the webcam when a button is pressed,
# and flash the LED when the process is active.
#
# Switch input: #1 (3.3 V)
# Switch output: Pin no. 11 (#4) 
# LED input: Pin no. 7 (#)
# 

# Espen Storheim, 30/08-2014.

import RPi.GPIO as GPIO
import subprocess
import os
import time


##################################################
# Trigger setup - External switch
##################################################

GPIO.setmode(GPIO.BOARD)

# Activate the internal pulldown resistor on pin 11
# to avoid a floating pin, i.e. sporadic trigging.
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set pin 7 to output.
GPIO.setup(7,GPIO.OUT)


##################################################
# Define a camera button function
##################################################
def camerabutton(n):
	filename = time.strftime("%Y%m%d_%H%M%S")+'.jpg'
	print "The camera has been triggered"
	os.system('raspistill -n -o %s' %(filename))
	time.sleep(5)

##################################################
# Wait for trigger and perform an action 
##################################################

# Try-loop: Set the LED output to the state of the
# button, i.e. button press = LED on.
try:
	while True:
		if GPIO.input(11)==1:
			GPIO.output(7, GPIO.input(11) )
			camerabutton(1)

		else:
			GPIO.output(7,0)

# Press Ctrl+C to cancel. This ensures that the GPIO pins are reset upon exit.
except KeyboardInterrupt:
	GPIO.cleanup()
	print '\n'
	print "Shutdown completed successfully!"
