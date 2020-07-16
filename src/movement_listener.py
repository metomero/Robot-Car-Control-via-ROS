#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

IN1 = 5
IN2 = 7
IN3 = 13
IN4 = 15
INSPD1 = 3
INSPD2 = 11

pins = [IN1, IN2, IN3, IN4]


GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(INSPD1, GPIO.OUT)
GPIO.setup(INSPD2, GPIO.OUT)

pwm1 = GPIO.PWM(INSPD1, 1000)
pwm2 = GPIO.PWM(INSPD2, 1000)

pwm1.start(100)
pwm2.start(100)

an_vals = [100, 100]

pwms = [pwm1, pwm2]

last_msg = "0,0,0,0,100,100"

def msg_callback(message):
    # get_caller_id(): Get fully resolved name of local node
    global last_msg
    rospy.loginfo(rospy.get_caller_id() + "Led Status %s", message.data)

    arr = str(message.data).split(',')

    if  arr != last_msg:
        
        last_msg = arr
##        GPIO.cleanup()
        
        for i in range(0, 4):
            if int(arr[i]) == 1:
                GPIO.output(pins[i], GPIO.HIGH)
            else:
                GPIO.output(pins[i], GPIO.LOW)

        for i in range(0, 2):
            val = int(arr[i + 4])
            dif = val - an_vals[i]
            
            
            print(i)
            print(val)
            print(dif)
            
            if (val != an_vals[i]):
                const = 1
                
                if val < an_vals[i]:
                    const = -1 * const
                    
                    
                for k in range(0,50):
                    pwms[i].ChangeDutyCycle( an_vals[i] + (k * const)) 
            
                an_vals[i]= val       
                
        

def listener():
    rospy.init_node('movement_listener', anonymous=True)

    rospy.Subscriber("message", String, msg_callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
    GPIO.cleanup()

