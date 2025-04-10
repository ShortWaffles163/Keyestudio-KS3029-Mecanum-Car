from machine import Pin, I2C
import time

# Import driver class
class Mecanum_Car_Driver_V2:
    def __init__(self):
        self.add = 0x30
        self.i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=400000)
        self.set_all_pwm(0)

    def set_pwm(self, ch, val):
        self.i2c.writeto(self.add, bytearray([ch, val & 0xFF]))

    def set_all_pwm(self, val):
        for ch in range(1, 9):
            self.set_pwm(ch, val)
