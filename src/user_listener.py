#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import socket
import threading
import time

Message = "0,0,0,0,100,100"
PORT = 65432

isConnected = False



class signalThread(threading.Thread):
    client = None
    isSend = 0
   
    def __init__(self, clt):
          global client
          threading.Thread.__init__(self)
          client = clt

    def run(self):
        try:
            while True:
                global client
                global Message
                data = client.recv(1024) # 1024 is the buffer size.
                dataStr = data.decode('utf-8')
                
                Message = dataStr
                
                if Message == 'Quit':
                    break
            
                print(Message)
                
            
        except BaseException as ex:
            pass
            #print("Error On Listening.")
            #print(ex)


def user_listener():
    pub = rospy.Publisher('message', String, queue_size=10)
    rospy.init_node('user_listener', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', PORT))
        
        s.listen(1)
        print("Waiting for connection.")

        conn, addr = s.accept()

        print(str(conn.getpeername()) + str(conn.getsockname()) + " connected.")
            
        time.sleep(0.2)
        
        pThread = signalThread(conn)
        pThread.start()
            
        while not rospy.is_shutdown():
                
            rospy.loginfo(Message)
            pub.publish(Message)
            rate.sleep()
            
            if Message == 'Quit':
                break
        
    except Exception as ex:
        print(ex)
        
    
    try:
        pThread.notify()
        conn.close()
        s.close()
    except:
        pass


if __name__ == '__main__':
    try:
        user_listener()
    except rospy.ROSInterruptException:
        pass
