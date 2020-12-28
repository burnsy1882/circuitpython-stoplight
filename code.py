##

import board
import digitalio
import time

# Variables
delay = 1.5

# Set leds to digital pins
red = digitalio.DigitalInOut(board.D1)
yellow = digitalio.DigitalInOut(board.D2)
green = digitalio.DigitalInOut(board.D3)

# Set directions for leds
red.direction = digitalio.Direction.OUTPUT
yellow.direction = digitalio.Direction.OUTPUT
green.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Run code
while True:
    
    # Red light
    red.value = True
    time.sleep(3 * delay)
    red.value = False
    
    # Green light
    green.value = True
    time.sleep(5 * delay)
    green.value = False
    
    # Yellow light
    yellow.value = True
    time.sleep(2 * delay)
    yellow.value = False
