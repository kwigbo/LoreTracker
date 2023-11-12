import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False

# ------------- Pulse

current_brightness = 0
reverse_fade = False

def pulse():
    global current_brightness
    global reverse_fade

    colors = themes[themeIndex]
    pulseColor = colors[0]

    if reverse_fade:
        current_brightness -= 0.025
    else:
        current_brightness += 0.025

    if current_brightness > 1:
        current_brightness = 1
        reverse_fade = True
    elif current_brightness < 0:
        reverse_fade = False
        current_brightness = 0

    cp.pixels.brightness = current_brightness

    pixelCount = len(cp.pixels)
    for x in range(pixelCount):
        cp.pixels[x] = pulseColor
    cp.pixels.show()
    time.sleep(0.05)

# ------------- Twirl

# colors = [0x, 0x, 0x, 0x, 0x]
rainbowTheme = [0xA800FF, 0x0079FF, 0x00F11D, 0xFFEF00, 0xFF7F00]
redTheme = [0xBA0222, 0xd70330, 0xfe0052, 0xFF40b7, 0xFd0188]
blueTheme = [0x0A8FBD, 0x40A6CD, 0x55BFD4, 0x80D3DD, 0xE1EBF1]
themes = [blueTheme, rainbowTheme, redTheme]

themeIndex = 0
colorOffset = 0
speed = 0.1

def getColor(index):
    colorCount = len(colors)
    currentColor = 0

    for currentIndex in range(index):
        currentColor += 1
        if currentColor >= colorCount:
            currentColor = 0

    return currentColor

def twirl():
    global colors
    global colorOffset
    pixelCount = len(cp.pixels)

    colors = themes[themeIndex]

    for pixel in range(pixelCount):
        colorIndex = colorOffset + pixel
        cp.pixels[pixel] = colors[getColor(colorIndex)]

    cp.pixels.show()
    colorOffset += 1
    if colorOffset > 4:
        colorOffset = 0
    time.sleep(speed)

lightMode = 0

while True:

    if cp.touch_A3:
        themeIndex -= 1
        time.sleep(0.2)

    if cp.touch_A4:
        themeIndex += 1
        time.sleep(0.2)

    totalThemes = len(themes)
    if themeIndex < 0:
        themeIndex = totalThemes - 1
    elif themeIndex == totalThemes:
        themeIndex = 0

    if cp.touch_A6:
        lightMode = 0
    elif cp.touch_A1:
        lightMode = 1

    if lightMode == 0:
        twirl()
    else:
        pulse()
