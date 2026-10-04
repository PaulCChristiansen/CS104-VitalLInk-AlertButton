from machine import Pin
import time

button = Pin(28, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("1",end=" ")
    else:
        print("0",end=" ")
    time.sleep(0.1) # Wait for USB to become ready


