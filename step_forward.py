from gpiozero import Servo
from time import sleep
import Inverse_Kinematics as ik

FRS_pin = 9
FLS_pin = 4
BRS_pin = 27
BLS_pin = 11

FRE_pin = 6
FLE_pin = 25
BRE_pin = 13
BLE_pin = 17


# Define your servo objects
servo1 = Servo(FRS_pin)
servo2 = Servo(FLS_pin)
servo3 = Servo(BRS_pin)
servo4 = Servo(BLS_pin)
servo5 = Servo(FRE_pin)
servo6 = Servo(FLE_pin)
servo7 = Servo(BRE_pin)
servo8 = Servo(BLE_pin)

def step():
    a1, a2 = ik.IK(0.122, 0.13, 0, 0.1)
    
    # Set the servo angles
    servo1.angle = 45
    servo5.angle = 120
    sleep(0.5)
    
    # Stop the servos
    servo1.angle = None
    servo5.angle = None
    
    # Set the angles back to the calculated values
    servo1.angle = a1
    servo5.angle = a2
    sleep(0.5)
    
    # Stop the servos
    servo1.angle = None
    servo5.angle = None

# You can call the 'step' function to perform the movement.
