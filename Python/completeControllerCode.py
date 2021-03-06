import pygame, sys, math
from pygame.locals import *

pygame.init()

### Tells the number of joysticks/error detection
joystick_count = pygame.joystick.get_count()
print ("There is ", joystick_count, "joystick/s")
if joystick_count == 0:
    print ("Error, I did not find any joysticks")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

def updateAxes():

    controllerDict = {'X-Axis1': 0, 'Y-Axis2': 0, 'X-Axis2': 0, 'Y-Axis2': 0};

    xAxis = my_joystick.get_axis(0) 
    yAxis = my_joystick.get_axis(1) * -1
    aAxis = my_joystick.get_axis(2)
    bAxis = my_joystick.get_axis(3) * -1

    if xAxis < 0.1 and xAxis > -0.1:
        xAxis = 0
    if yAxis < 0.1 and yAxis > -0.1:
        yAxis = 0
    if aAxis < 0.1 and aAxis > -0.1:
        aAxis = 0
    if bAxis < 0.1 and bAxis > -0.1:
        bAxis = 0

    xAxis = math.ceil(xAxis*10000)/10000
    yAxis = math.ceil(yAxis*10000)/10000
    aAxis = math.ceil(aAxis*10000)/10000
    bAxis = math.ceil(bAxis*10000)/10000

    print 'X-Axis 1: ' + str(xAxis) + '  Y-Axis 1: ' + str(yAxis)
    print 'X-Axis 2: ' + str(aAxis) + '  Y-Axis 2: ' + str(bAxis)

    controllerDict['X-Axis1'] = xAxis;
    controllerDict['Y-Axis1'] = yAxis;
    controllerDict['X-Axis2'] = aAxis;
    controllerDict['Y-Axis2'] = bAxis;

    print "dict['X-Axis1']: ", controllerDict['X-Axis1'];

    return controllerDict

def updateButtons():

    buttonDict = {'xButton': 0, 'circleButton': 0, 'triangleButton': 0, 'squareButton': 0,
    'leftBumper': 0, 'rightBumper': 0, 'leftTrigger': 0, 'rightTrigger': 0,
    'selectButton': 0, 'startButton': 0, 'leftToggle': 0, 'rightToggle': 0,};

    xButton = my_joystick.get_button(1)
    circleButton = my_joystick.get_button(2)
    triangleButton = my_joystick.get_button(3)
    squareButton = my_joystick.get_button(0)
    leftBumper = my_joystick.get_button(4)
    rightBumper = my_joystick.get_button(5)
    leftTrigger = my_joystick.get_button(6)
    rightTrigger = my_joystick.get_button(7)
    selectButton = my_joystick.get_button(8)
    startButton = my_joystick.get_button(9)
    leftToggle = my_joystick.get_button(10)
    rightToggle = my_joystick.get_button(11)

    print 'X Button is: ' + str(xButton) + '  Circle Button is: ' + str(circleButton)
    print 'Triangle Button is: ' + str(triangleButton) + '  Square Button is: ' + str(squareButton)
    print 'Left Bumper is: ' + str(leftBumper) + '  Right Bumper is: ' + str(rightBumper)
    print 'Left Trigger is: ' + str(leftTrigger) + '  Right Trigger is: ' + str(rightTrigger)
    print 'Select Button is: ' + str(selectButton) + '  Start Button is: ' + str(startButton)
    print 'Left Toggle is: ' + str(leftToggle) + '  Right Toggle is: ' + str(rightToggle)

    buttonDict['xButton'] = xButton;
    buttonDict['circleButton'] = circleButton;
    buttonDict['triangleButton'] = triangleButton;
    buttonDict['squareButton'] = squareButton;
    buttonDict['leftBumper'] = leftBumper;
    buttonDict['rightBumper'] = rightBumper;
    buttonDict['leftTrigger'] = leftTrigger;
    buttonDict['rightTrigger'] = rightTrigger;
    buttonDict['selectButton'] = selectButton;
    buttonDict['startButton'] = startButton;
    buttonDict['leftToggle'] = leftToggle;
    buttonDict['rightToggle'] = rightToggle;

    print "dict['xButton']: ", buttonDict['xButton'];

    return buttonDict

while True:
    pygame.event.pump()

    updateAxes()
    updateButtons()

    pygame.time.wait(300)
