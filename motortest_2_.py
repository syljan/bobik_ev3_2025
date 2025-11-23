#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B,SpeedPercent

m1 = LargeMotor(OUTPUT_A)
m1.on_for_rotations(SpeedPercent(75), 5)

m2 = LargeMotor(OUTPUT_B)
m2.on_for_rotations(SpeedPercent(75), 5)