import turtle
import time
skibiditoilet=turtle.Turtle()
skibiditoilet.shape('arrow')
skibiditoilet.speed(0)
skibiditoilet.hideturtle()

s=turtle.Screen()

while True:
    for i in range(40):
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001999999989988998988989898898999888988989889898988989899878889989988889888998898899898899898898989888898989898899898898989000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        if i % 2 == 0:
            s.bgcolor('red')
        else:
            s.bgcolor('lime')  

    #1st circle
    skibiditoilet.penup()
    skibiditoilet.goto(0,-200)
    skibiditoilet.pendown()
    skibiditoilet.begin_fill()
    skibiditoilet.color('white')
    skibiditoilet.circle(80)
    skibiditoilet.end_fill()

    #2nd circle
    skibiditoilet.penup()
    skibiditoilet.goto(0,-40)
    skibiditoilet.pendown()
    skibiditoilet.begin_fill()
    skibiditoilet.color('white')
    skibiditoilet.circle(50)
    skibiditoilet.end_fill()

    #3rd head
    skibiditoilet.penup()
    skibiditoilet.goto(0,60)
    skibiditoilet.pendown()
    skibiditoilet.begin_fill()
    skibiditoilet.color('white')
    skibiditoilet.circle(30)
    skibiditoilet.end_fill()

    skibiditoilet.penup()
    skibiditoilet.goto(0,75)
    skibiditoilet.pendown()
    skibiditoilet.begin_fill()
    skibiditoilet.color('black')
    skibiditoilet