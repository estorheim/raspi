# Make a LED light up when a button is pressed.
#
# Switch input: #1 (3.3 V)
# Switch output: Pin no. 11 (#4) 
# LED input: Pin no. 7 (#)
# 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Activate the internal pulldown resistor on pin 11
# to avoid a floating pin.
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set pin 7 to output.
GPIO.setup(7,GPIO.OUT)

# Try-loop: Set the LED output to the state of the
# button, i.e. button press = LED on.
try:
	while True:
		GPIO.output(7, GPIO.input(11) )

# Press Ctrl+C to cancel. This ensures that the GPIO
# pins are reset upon exit.
except KeyboardInterrupt:
	GPIO.cleanup()
