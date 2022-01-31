import busio
import board
import time
import RPi.GPIO as GPIO
from PCF8574.lcd import LCD
from PCF8574.pcf8574 import PCF8574

# GPIO pins of the buttons
S1 = 4
S2 = 16
S3 = 10
S4 = 9
inputs = [S1, S2, S3, S4]
GPIO.setmode(GPIO.BCM)

# setting up buttons as inputs
for switch in inputs:
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up lcd
lcd = LCD(PCF8574(busio.I2C(board.SCL, board.SDA),0x27), num_rows=4, num_cols=20)

column = 0

def checkSwitches():
    #Check status of all four switches on the LCD board
    val1 = not GPIO.input(S1)
    val2 = not GPIO.input(S2)
    val3 = not GPIO.input(S3)
    val4 = not GPIO.input(S4)

    if val1 == GPIO.HIGH:
        return "S1"
    elif val2 == GPIO.HIGH:
        return "S2"
    elif val3 == GPIO.HIGH:
        return "S3"
    elif val4 == GPIO.HIGH:
        return "S4"
    return "0"


try:
    lcd.print("Press a button!")
    while(True):
        value = checkSwitches()
        # nothing is pressed
        if value == "0":
            continue

        if column == 0:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("You pressed "+value+"!")
            column += 1
        elif column == 1:
            lcd.set_cursor_pos(1, 0)
            lcd.print("You pressed "+value+"!")
            column += 1
        elif column == 2:
            lcd.set_cursor_pos(2, 0)
            lcd.print("You pressed "+value+"!")
            column += 1
        elif column == 3:
            lcd.set_cursor_pos(3, 0)
            lcd.print("You pressed "+value+"!")
            column -= 3
        time.sleep(1)


except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
