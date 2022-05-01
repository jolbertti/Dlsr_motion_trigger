from machine import Pin
import time

#delay between shutter release signals sent to camera
#REPLACE WITH INPUT FROM SWITCH
shotdelay = 4

#how many shutter release signals are sent to camera
#REPLACE WITH INPUT FROM SWITCH
photos = 5

#delay from initial pir signal to shutter release signal sent to camera 
#REPLACE WITH INPUT FROM SWITCH
wakeup = 2


pir = Pin(22, Pin.IN, Pin.PULL_DOWN)
 
#print('Starting up the PIR Module')
#time.sleep(1)
#print('Ready')

while True:
    if pir.value() == 1:
        time.sleep(wakeup)
        for i in range(photos):
            print('Click nro' ,i)
            time.sleep(shotdelay)
