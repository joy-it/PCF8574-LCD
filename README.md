# PCF8574-LCD
### Raspberry Pi Python3 library for RB-LCD-16x2 and RB-LCD-20x4
This library is based on the [CircuitPython_LCD](https://github.com/dhalbert/CircuitPython_LCD/) library by [dhalbert](https://github.com/dhalbert/). The changes were necessary because of a different pinout used with the PCF8574 and a HD44780.

Pinout
=====

|    PCF8574    |      LCD      |
| ------------- |:-------------:|
|       P0      |       D4      |
|       P1      |       D5      |
|       P2      |       D6      |     
|       P3      |       D7      |
|       P4      |       RS      |
|       P5      |       RW      |
|       P6      |       --      |
|       P7      |       EN      |

Dependencies
=====

Before you install the library you need to activate i2c on your Raspberry Pi and install the following dependencies.

    sudo apt-get install i2c-tools python3-smbus libi2c-dev python3-pip

    sudo pip3 install RPi.GPIO

Installation
=====

    git clone https://github.com/joy-it/PCF8574-LCD.git

    cd ~/PCF8574-LCD/

    sudo python3 setup.py install

**Examples**

    cd ~/PCF8574-LCD/examples/

**RB-LCD-16x2**

    python3 example-16x2.py

**RB-LCD-20x4**

    python3 example-20x4.py


Library functions
=====

- `lcd.close()` - closes LCD class
- `lcd.set_display_enabled(value)` - set display on and off with value: 0-off, 1-on
- `lcd.set_cursor_mode(value)` - sets cursor mode with value: 0-off, 1-blinks, 2-line
- `lcd.set_cursor_pos(row, column)`- sets cursor to position: row, column
- `lcd.print(string)` - prints String
- `lcd.clear()` - clears display
- `lcd.home()` - sets cursor to home position
- `lcd.shift_display(amount)` - shifts display with amount
- `lcd.create_char(location, bitmap)`- creates character with bitmap and location
