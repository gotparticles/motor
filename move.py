import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 17
 
GPIO.setup(Motor1A)

print("Turning motor on")
GPIO.output(Motor1A)
 
sleep(2)

GPIO.cleanup()
