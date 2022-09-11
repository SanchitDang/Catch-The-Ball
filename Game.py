import random
import turtle
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Catch The ball")
canvas = tkinter.Canvas(master=window, width=900, height=800)
canvas.pack()


def CTB():
    # Turtles
    sp = turtle.RawTurtle(canvas)
    bucket = turtle.RawTurtle(canvas)
    border = turtle.RawTurtle(canvas)
    over = turtle.RawTurtle(canvas)
    pen = turtle.RawTurtle(canvas)

    # Border
    border.hideturtle()
    border.color('blue')
    border.speed(0)
    border.penup()
    border.setposition(-400, -350)
    border.pendown()
    border.pensize(4)

    # Rectangular border shape
    border.forward(800)
    border.left(90)
    border.forward(650)
    border.left(90)
    border.forward(800)
    border.left(90)
    border.forward(650)
    border.left(90)

    # Bucket
    bucket.speed(0)
    bucket.penup()
    bucket.shape('square')
    bucket.sety(-300)
    bucket.shapesize(4, 4, 0)

    # Sp Start Pos
    sp.speed(0)
    sp.penup()
    sp.sety(300)
    sp.shape('circle')
    sp.color('green')
    sp.shapesize(2)

    # Commands
    def leftKey(event):
        x = bucket.xcor()
        x -= 40
        bucket.setx(x)

    def rightKey(event):
        x = bucket.xcor()
        x += 40
        bucket.setx(x)

    window.bind('<Left>', leftKey)
    window.bind('<Right>', rightKey)

    # Sp At Top X-axis
    sp.speed(0)     # Speed of roaming at upper X axis
    sp.setx(random.randrange(-300, 300))    # Ball at any random position in topmost x axis
    sp.setheading(270)
    sp.speed(1)     # Speed of falling first time

    # Score
    pen.hideturtle()
    score = 0
    pen.penup()
    pen.goto(-360, 305)
    pen.write("score:{}".format(score), font=("courier", 24, "normal"))  # write 0 score

    # Game Over
    over.hideturtle()
    over.pu()
    over.color('black')
    over.goto(-200, -50)

    # Catching Sp in Bucket
    while True:
        sp.setx(random.randrange(-300, 300))
        sp.fd(610)
        sp.speed(1)

        while True:
            if ((sp.xcor() - bucket.xcor()) ** 2 + (sp.ycor() - bucket.ycor()) ** 2) ** 1 / 2 <= 700:   # Collision
                pen.clear()  # Clears old score
                score += 1
                pen.write("score:{}".format(score), font=("courier", 24, "normal"))   # writes new score
                sp.speed(0)
                sp.sety(300)
                sp.setx(random.randrange(-300, 300))
                sp.speed(1)
                sp.fd(610)
            else:

                sp.hideturtle()
                bucket.hideturtle()
                over.write('GAME OVER', font=('Eras BoldITC', 50, "normal"))

                ans = messagebox.askyesno("Game Over", "Do You Want To Play Again?")
                if ans is True:
                    over.clear()
                    pen.clear()
                    CTB()
                else:
                    quit()


CTB()
window.mainloop()
