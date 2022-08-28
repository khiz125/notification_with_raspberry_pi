import requests
import RPi.GPIO as GPIO
import time
import sys
import os
from dotenv import load_dotenv
load_dotenv()

# set val to GPIO PORT number
RED_GPIO = 24
BLUE_GPIO = 25

# GPIO.BCM: to handles GPIO PORT number
GPIO.setmode(GPIO.BCM)

# GPIO set up
# pull_up_down=GPIO.PUD_DOWN => set GPIO status is "0"（Low）
GPIO.setup(RED_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BLUE_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# flag of button ( on / off )
LastStatus = False

while True:
    try:
        # Checking status of GPIO PORT with infinite while loop
        RED_SwitchStatus = GPIO.input(RED_GPIO)
        BLUE_SwitchStatus = GPIO.input(BLUE_GPIO)

        # If red or blue button pushed, 3.3v changes GPIO.input  to "1"（High）
        if LastStatus != RED_SwitchStatus:         
            if RED_SwitchStatus == 1:
                print("Red button LINE send")
                
                #LINE notify
                url = 'https://notify-api.line.me/api/notify'
                token = os.environ['LINE_NOTIFY_TOKEN']
                headers = {"Authorization" : "Bearer "+ token} 
                message =  "Red button pushed!!" 
                payload = {"message" :  message} 
                r = requests.post(url, headers = headers, params=payload)
            time.sleep(0.2)
                
        elif LastStatus != BLUE_SwitchStatus:
            if BLUE_SwitchStatus == 1:
                print("Blue button LINE send")
                
                #LINE notify
                url = 'https://notify-api.line.me/api/notify'
                token = os.environ['LINE_NOTIFY_TOKEN']
                headers = {"Authorization" : "Bearer "+ token} 
                message =  "Blue button pushed!!" 
                payload = {"message" :  message} 
                r = requests.post(url, headers = headers, params=payload)
                
            time.sleep(0.2)
        LastStatus = False
         
    # Press "Ctrl+C" and stop while loop
    except KeyboardInterrupt:
        # Clean up GPIO port status
        GPIO.cleanup()
        sys.exit()