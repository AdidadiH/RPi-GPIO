#!/usr/bin/env python3

LED_PIN = 25

import time
import RPi.GPIO as IO
import os

#
#setup for GPIO Pins
#
def setupIO():
    IO.setmode(IO.BCM)
    IO.setwarnings(False)

    IO.setup(LED_PIN, IO.OUT)


#
#set led to bool state
#
def setLed(state):

  if(state):
    IO.output(LED_PIN, IO.HIGH)
  else:
    IO.output(LED_PIN, IO.LOW)


#
#loop for eternity
#
def loop():

  #blink led with 1s delay
  while(True):

    setLed(True)
    time.sleep(1)

    setLed(False)
    time.sleep(1)


#---------------------------MAIN---------------------------

setupIO()
loop()
