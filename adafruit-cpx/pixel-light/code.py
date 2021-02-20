from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.01

pixelsToLight = 0

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
off = (0, 0, 0)

color = white

while True:
    if cp.button_b and pixelsToLight < 10:
        pixelsToLight = pixelsToLight + 1
    elif cp.button_a and pixelsToLight > 0:
        pixelsToLight = pixelsToLight - 1

    if cp.touch_A1:
        color = green
    elif cp.touch_A2:
        color = blue
    elif cp.touch_A3:
        color = red
    elif cp.touch_A7:
        color = white

    cp.pixels[0:pixelsToLight] = [color] * pixelsToLight
    cp.pixels[pixelsToLight:10] = [off] * (10-pixelsToLight)
    print(color)
    time.sleep(0.2)

