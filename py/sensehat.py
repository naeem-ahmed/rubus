from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

print(sense.humidity)
print(sense.pressure)
print(sense.temperature)

for r in range(0, 255):
    sense.clear(r,0,0)
    sleep(0.05)

for g in range(0, 255):
    sense.clear(255,g,0)
    sleep(0.05)

for b in range(0, 255):
    sense.clear(255,255,b)
    sleep(0.05)

sense.clear(0,0,0)

#sense.low_light = True
#sleep(2)
#sense.low_light = False

