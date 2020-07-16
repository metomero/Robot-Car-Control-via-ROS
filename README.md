# Robot Car Control via ROS
In this project we control a car with an application. The car we are going to control has a Raspberry Pi and a motor driver attached to it. Raspberry Pi provides the control of the car by giving the motor driver the necessary values ​​according to the message received from the user.

# Prerequirements
First of all, we need some electronic parts to build it.

- Raspberry Pi 3
- L298N Motor Driver
- 12 V DC Motor (4)
- 12 V Power Source or Battery

## What is ROS

The Robot Operating System (ROS) is an open-source framework that helps researchers and developers build and reuse code between robotics applications. ROS is also a global open-source community of engineers, developers and hobbyists who contribute to making robots better, more accessible and available to everyone.

For mor info;
[http://wiki.ros.org/ROS/Introduction](http://wiki.ros.org/ROS/Introduction)

## Setup ROS

  
You can install the system by following the steps in [this link]([http://wiki.ros.org/ROS/Installation](http://wiki.ros.org/ROS/Installation)).

# Circuit Diagram
![L298N Driver](https://i.hizliresim.com/4YOJf5.png)

If we look at the motor connection, the two engines at the top and the two engines at the bottom are connected to the same sources. We can think of it as single engines.

![L298N Driver](https://i.hizliresim.com/iuz6Se.png)
In addition to activating the motors, the activation pins (ENA, ENB) will determine the rotational speed of the motors, which we will give between 0 and 5 volts. We will use PWM signals to get these analog values.

IN1 and IN2 pins determine the direction the first motor (MOTOR A) will turn. For our example;

>Forward -> IN1 = 1, IN2 = 0
>Backward -> IN1 = 0, IN2 = 1

Likewise, both pins determine the direction of rotation of the second motor. For our example;
>Forward -> IN3 = 1, IN4 = 0
>Backward -> IN3 = 0, IN4 = 1

In this project, I used an enum class that defines movements in the android program. According to the keys pressed, it sends one of these movements to the system. But since I don't think this method is a good method, I will change it later.

# How does system works?

We have an android application. When this application is opened, it requests the IP address of the system that our car is connected to. It connects to the system after entering its IP address.

ROS is running in our system. Publisher (user_listener.py) waits for messages from the app. Transmits the incoming motion message to the Subscriber (movement_listener.py). The subscriber parse the message and runs the motor driver with this information. Finally the car moves, simple.

# Android App

You can find the Android application from this link;


# Start System

Copy the necessary files for ROS to your workspace.
```
$ cd catkin_ws/src
$ git clone https://github.com/metomero/Robot-Car-Control-via-ROS.git
```

Configure the project.
```
$ cd ..
$ cd catkin_make
```

Install the phone app.Make sure the system is on the same network as the phone.

Run ROS in the system.
```
$ roscore
```

Run the publisher and subscriber in separate terminals.
```
$ rosrun ros_car_project user_listener.py
```

```
$ rosrun ros_car_project movement_listener.py
```

Enter the IP address of the system into the application.You can use the command below to learn the IP address of the system.

```
$ ifconfig
```
