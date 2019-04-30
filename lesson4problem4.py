from turtle import *

sourpatch = Turtle()

sourpatch.color("red")
sourpatch.pensize(12)
sourpatch.speed(10)
sourpatch.shape("turtle")

sourpatch.circle(25)



from turtle import *

stardust = Turtle()

stardust.color("blue")
stardust.pensize(12)
stardust.speed(10)
stardust.shape("turtle")

for x in range(3):
	stardust.forward(100)
	stardust.left(120)

mainloop()