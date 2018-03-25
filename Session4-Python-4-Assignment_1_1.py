# -*- coding: utf-8 -*-
"""
@author: Ravikiran Bailkeri
Problem:
    Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
"""


import math

class Triangle:
    def __init__(self, a,b,c):
        self.a = float(input('Please Enter the First side of a Triangle: '))
        self.b = float(input('Please Enter the First side of a Triangle: '))
        self.c = float(input('Please Enter the First side of a Triangle: '))

# Inheritance- Subclass
                    
class TriArea(Triangle):
    def __init__(self):
        Triangle.__init__(self,a,b,c)

    def findArea(self):
        a = self.a
        b= self.b
        c = self.c
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(area, 'is the area of the triangle')

t = TriArea()
t.findArea()

