#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from xarm.wrapper import XArmAPI

"""
Move joint,
    1. explicit setting is_radian=False, set the default unit is degree (°) (not radian)
    set_servo_angle: 
        1. explicit setting wait=True to wait for the arm to complete
"""

xarm = XArmAPI('192.168.1.113', is_radian=False)
xarm.motion_enable(enable=True)
xarm.set_state(state=0)

xarm.reset(wait=True)

xarm.set_servo_angle(angle=[60, 0, 0, 0, 0, 0, 0], speed=30, wait=True)
print(xarm.get_servo_angle(is_radian=False))
xarm.set_servo_angle(angle=[60, -45, 0, 0, 0, 0, 0], speed=30, wait=True)
print(xarm.get_servo_angle(is_radian=False))
xarm.set_servo_angle(angle=[60, -45, 0, -60, 0, 0, 0], speed=30, wait=True)
print(xarm.get_servo_angle(is_radian=False))
xarm.set_servo_angle(angle=[45, -45, -30, -60, 0, 0, 0], speed=30, wait=True)
print(xarm.get_servo_angle(is_radian=False))
xarm.set_servo_angle(angle=[-45, -45, 0, 0, 0, 0, 0], speed=30, wait=True)
print(xarm.get_servo_angle(is_radian=False))
xarm.set_servo_angle(angle=[0, 0, 0, 0, 0, 0, 0], speed=30, wait=True)
print(xarm.get_servo_angle(is_radian=False))

xarm.disconnect()
