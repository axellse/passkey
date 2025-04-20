import neopixel
import json
import board
import time
import thisbutton as tb
import usb_hid
from adafruit_hid.keyboard import Keyboard
import keyboard_layout_win_sw
from keycode_win_sw import Keycode
import digitalio
import board
import pwmio

keyboard = Keyboard(usb_hid.devices)
layout = keyboard_layout_win_sw.KeyboardLayout(keyboard)
buzzer = pwmio.PWMOut(board.GP28, variable_frequency=True)
led = neopixel.NeoPixel(board.GP24, 8)
button = tb.thisButton(board.GP19, True)
toggleButton = tb.thisButton(board.GP25, True)
toggleLed = digitalio.DigitalInOut(board.GP23)
toggleLed.direction = digitalio.Direction.OUTPUT

itemColors = [
    (255, 0, 0), #Red
    (255, 0, 255), #Pink
    (255, 255, 0), #Yellow
    (0, 255, 255), #Blue
    (255, 255, 255),#White
    (0, 255, 0),#Green
    (128,0,128), #Purple
    (255, 140, 0), #Orange
]
squareWave = 2**15

selectedItem = 0
newLines = True

led[0] = itemColors[selectedItem]
led.write()

def buzz(freq):
    buzzer.frequency = freq
    buzzer.duty_cycle = squareWave
def buzzoff():
    buzzer.duty_cycle = 0
def buzzfor(tm, freq):
    buzz(freq)
    time.sleep(tm)
    buzzoff()

def buttonRel():
    global selectedItem
    if (selectedItem == len(itemColors) -1):
        selectedItem = 0
    else:
        selectedItem = selectedItem + 1
    led[0] = itemColors[selectedItem]
    led.write()
    buzzfor(0.1, 880)
def toggleNewline():
    global newLines
    newLines = not newLines
    toggleLed.value = not newLines
    
    freqs = [330, 550]
    if not newLines:
        freqs = list(reversed(freqs))
    buzzfor(0.1, freqs[0])
    buzzfor(0.1, freqs[1])
def writePass():
    passes = json.loads(open('pass.json').read())
    if len(passes) > selectedItem:
        buzz(1220)
        layout.write(passes[selectedItem])
        if newLines:
            layout.write('\n')
        buzzoff()
    else:
        buzzfor(0.5, 200)
        print("password not defined")
button.assignClick(buttonRel)
toggleButton.assignClick(toggleNewline)
button.assignLongPressStart(writePass)

while True:
    button.tick()
    toggleButton.tick()