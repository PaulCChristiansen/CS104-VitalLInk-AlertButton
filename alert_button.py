from machine import Pin
import time

# Configure button on GPIO 28 with a pull-down resistor
button = Pin(28, Pin.IN, Pin.PULL_DOWN)

# State variable to track whether the button is currently pressed
button_pressed = False

while True:
    # Check if the button is pressed and was not already pressed
    if button.value() == 1 and not button_pressed:
        print("Alert: Button pressed!")
        button_pressed = True  # Mark state as pressed to prevent repeated triggers
    
    # Reset the state when the button is released
    elif button.value() == 0 and button_pressed:
        button_pressed = False

    # Short delay for debouncing and loop optimization
    time.sleep(0.05)


