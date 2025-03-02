""" test_info : connect a SeeSaw throught I2C bus then read information from it """

from machine import I2C, Pin
from seesaw import Seesaw

i2c = I2C( 1, sda=Pin.board.GP6, scl=Pin.board.GP7 )

# Parameter are named for a better comprehension
s = Seesaw( i2c=i2c, addr=0x2e, drdy=None, reset=True) # NeoTrellis addr, readypin, soft_reset
print( "chip_id     :", s.chip_id )
print( "pid         :", s.get_version()>>16 , "(product id)")
print( "version     :", s.get_version() )
print( "pin_mapping :", s.pin_mapping )

