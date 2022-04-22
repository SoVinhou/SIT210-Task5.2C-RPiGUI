from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##HardWare
Redled = LED(18)
Blueled = LED(17)
Greenled = LED(25)

##GUI
win = Tk() ##Create a Window
win.title("GUI LED TOGGLER")
myFont = tkinter.font.Font(family = 'Arial', size = 16, weight = "bold")

## EVENT
def RedledToggler():
    if Redled.is_lit:
        Redled.off()
        RedLedToggleButton["text"] = "Turn Red LED On"
    else:
        Redled.on()
        RedLedToggleButton["text"] = "Turn Red LED Off"

def BlueledToggler():
    if Blueled.is_lit:
        Blueled.off()
        BlueLedToggleButton["text"] = "Turn Blue LED On"
    else:
        Blueled.on()
        BlueLedToggleButton["text"] = "Turn Blue LED Off"
        
def GreenledToggler():
    if Greenled.is_lit:
        Greenled.off()
        GreenLedToggleButton["text"] = "Turn Green LED On"
    else:
        Greenled.on()
        GreenLedToggleButton["text"] = "Turn Green LED Off"
        


## CREATE WIDGETS
RedLedToggleButton = Button(win, text = 'Turn Red LED On', font = myFont, command = RedledToggler, bg = 'Red', height = 1, width = 50) ## CREATE RED LED WIDGET
RedLedToggleButton.grid(row=0,column=1)

BlueLedToggleButton = Button(win, text = 'Turn Blue LED On', font = myFont, command = BlueledToggler, bg = 'Blue', height = 1, width = 50) ## CREATE BLUE LED WIDGET
BlueLedToggleButton.grid(row=1,column=1)

GreenLedToggleButton = Button(win, text = 'Turn Green LED On', font = myFont, command = GreenledToggler, bg = 'Green', height = 1, width = 50) ## CREATE BLUE LED WIDGET
GreenLedToggleButton.grid(row=2,column=1)

