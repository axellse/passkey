import board
import digitalio
import storage

btn = digitalio.DigitalInOut(board.GP19)

btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

if btn.value == True:
    storage.disable_usb_drive()