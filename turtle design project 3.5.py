import turtle
from myFunc import *
from random import randint

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

turtle.bgcolor(102,102,255)

randomStars(bob)

move(bob,0,0)
flowerp1(bob)
move(bob,-30,-110)
flowerp2(bob)
move(bob,-100,-150)
flowerp3(bob)
move(bob,-30,10)
flowerp4(bob)


