from turtle import *

stardust = Turtle()

stardust.color("yellow")
stardust.pensize(12)
stardust.speed(10)
stardust.shape("turtle")
 
screen = Screen()
screen.bgcolor("red")

stardust.forward(80)
stardust.right(50)
stardust.forward(200)
stardust.left(150)
stardust.forward(50)
stardust.circle(25)
stardust.backwards(300)

mainloop()