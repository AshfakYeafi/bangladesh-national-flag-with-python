import time
import turtle
from pygame import mixer
turtle.setup(1000,700)
turtle.title("Bangladesh National Flag @Ashfak Yeafi")
t=turtle.Turtle()
mixer.init()
mixer.music.load('song.ogg')
mixer.music.play()

t.pensize(5)

height=500
weight= height * (10 / 6)
radius= weight / 5

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.begin_fill()
t.color('#006a4e')
t.speed(1)
t.forward(weight / 2)
t.right(90)
t.forward(height/2)
t.left(90)
t.backward(weight)
t.left(90)
t.forward(height)
t.right(90)
t.forward(weight)
t.right(90)
t.forward(height/2)
t.end_fill()

move(0,0)
t.color('#f42a41')
t.speed(5)
t.begin_fill()

for i in range(360):
    t.forward(radius)
    t.backward(radius)
    t.left(1)
move(-radius,0)
t.circle(radius,360)
t.end_fill()
time.sleep(10)
