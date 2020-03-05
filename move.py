import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 17
 
GPIO.setup(Motor1A,GPIO.right)

print("Turning motor on")
GPIO.output(Motor1A,GPIO.right)
 
sleep(2)

GPIO.cleanup()
