# passkey
a simple passkey style device to automatically enter long and unmemorable passwords for you, made with the [Orpheus Pico](https://orpheuspico.hackclub.com/).

<img width="400" src="https://github.com/user-attachments/assets/af16cc60-d1d3-47e2-8ff9-a9e4031808e1"> </img>
## About
It can store up to 8 passwords in total, which are easily set through a JSON file that can be edited by holding down the large button while plugging in the device. Pick the password you want to use using the large button on the front and see which password is currently selected with the RGB LED on the back. Once you have selected your password, hold the button down to enter it. It also features a small buzzer on the front and a button to toggle writing a newline once it's done writing out your password to log you in.
## Building the device and flashing the firmware
You only need three separate components to build the device:
* An [Orpheus Pico](https://orpheuspico.hackclub.com/)
* A [passive buzzer](https://www.electrokit.com/en/piezoelement-12x8.5mm-passiv)
* A [COM-09190](https://www.digikey.se/sv/products/detail/sparkfun-electronics/COM-09190/14671654?srsltid=AfmBOoqAxP6nLFY3OoAQI8lKrYYXItYvFcEovX7zmepL6Kru_ZDl1CI2) button or similar

### Soldering the buzzer
First off, cut off the legs of the buzzer, and solder wires to the pads around the legs. Route the wires out the side of the buzzer, and into ground and pin 25. Finally, glue the buzzer onto the board.

<img height="300" src="https://github.com/user-attachments/assets/a6d769a1-6e11-4af5-b8de-dd968c327c96"></img>
### Soldering the button
First, make sure the button is oriented like in the picture below. Then bend all the legs of the button so that they point out the sides instead of down, press the button down so it sits flush with the board and cut off the top right pin. Finally, solder both bottom legs of the button to the ground pins on both sides of the board, and the top left leg to pin 19.

<img height="300" src="https://github.com/user-attachments/assets/35aa6307-afe5-4bb0-a5a0-eecec141f15c"></img>
### Flashing the firmware
First up, [download CircuitPython to your board.](https://circuitpython.org/board/raspberry_pi_pico/)

Then, upload the contents of this repository including the lib folder, code.py and boot.py. Disconnecting and reconnecting the device now, it should not pop up as a drive like it did previously.
### Uploading your passwords
If you hold the large button down while plugging in the device, it should appear as a drive like in the beginning. Here, create a pass.json file and structure it like an array of strings, for example:
```
[
  "password 1",
  "password 2",
  "etc..."
]
```
You can create up to 8 passwords here. The order is the same order that the colors are in, that is:
| Color    |
| -------- |
| Red  |
| Pink |
| Yellow    |
| Blue    |
| White    |
| Green    |
| Purple    |
| Orange    |
### Done
With the file created, you're done! Test the device out, and if you have encountered any issues, lmk via the issue tracker!
