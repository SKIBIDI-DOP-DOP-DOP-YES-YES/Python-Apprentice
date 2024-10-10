
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
import turtle
tina= turtle
tina.speed (1)
tina.pendown
tina.begin_fill()
tina.color('red')
tina.forward(250)
tina.left(90)
tina.forward(250)
tina.left(90)
tina.forward(250)
tina.left(90)
tina.forward(250)
tina.left(90)
tina.forward(125)
tina.end_fill()
tina.fillcolor('red')
tina.left(90)
tina.forward(25)
tina.right(90)

tina.penup()
tina.pendown()
tina.begin_fill()
tina.fillcolor('white')
tina.circle(75)
tina.forward(50)
tina.left(45)
tina.end_fill()
turtle.exitonclick()
