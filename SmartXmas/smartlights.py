import speech_recognition as sr
import time

from gpiozero import Button

import board
import neopixel

button = Button(21)

# speech recognition settings
r = sr.Recognizer()
m = sr.Microphone()

# LED strip configuration:
LED_COUNT   = 90      # Number of LED pixels.
LED_PIN     = board.D18      # GPIO pin
LED_BRIGHTNESS = 0.2  # LED brightness
LED_ORDER = neopixel.GRB # order of LED colours. May also be GRB, GRBW, or RGBW

# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write=False, pixel_order = LED_ORDER)

# Setting variables for a specific sequence
red = (255,0,0)
green = (0,255,0)
flip = 0

# Function to make an alternating series of lights
def merrychristmas():
    global flip
    for i in range(90):
        if flip == 0:
            strip[i] = red
            flip = 1
        else:
            strip[i] = green
            flip = 0
    strip.show()

while True:
    button.wait_for_press()
    button.wait_for_release()
    
	# set the audio source
	
    with m as source: audio = r.listen(source)
    
    # recognize speech using Google Speech Recognition
    value = r.recognize_google(audio)

    # check the speech against trigger words
    if value == 'lights on':
        strip.fill((255,255,255))
        strip.show()
        
    if value == 'lights off':
        strip.fill((0,0,0))
        strip.show()
        
    if value == 'Merry Christmas':
        merrychristmas()