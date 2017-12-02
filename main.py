import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)

pwm=GPIO.PWM(03, 50)

pwm.start(0)

def SetAngle(angle):
    duty = angle /18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

def lock():
    SetAngle(0)

def unlock():
    SetAngle(180)

def main():
    if sys.argv[1] == 'open':
        unlock()
    elif sys.argv[1] == 'close':
        lock()

main()

pwm.stop()
GPIO.cleanup()
