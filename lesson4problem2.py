from turtle import *

stardust = Turtle()

stardust.color("blue")
stardust.pensize(12)
stardust.speed(10)
stardust.shape("turtle")

for x in range(4):
	stardust.forward(100)
	stardust.left(90)

mainloop()