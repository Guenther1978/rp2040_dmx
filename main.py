# main.py
from machine import Timer
import dmx
import led

dmx1 = dmx.universe(1)
rgb = led.Rgb(8, 9, 10)

def updater(t):
    for i in rgb.list_leds:
        i.change_intensity()
        dmx1.set_channels({i.address:i.intensity})
    dmx1.write_frame()

tim = Timer()
tim.init(period=1000, mode=Timer.PERIODIC, callback=updater)

