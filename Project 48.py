import turtle
import random
import time

#Background
bg = turtle.Screen()
bg.bgcolor("White")
bg.title("Turtle crossing")

#Player
bg.tracer(0)
crossing_turtle = turtle.Turtle()
crossing_turtle.shape("turtle")
crossing_turtle.pu()
crossing_turtle.seth(90)
crossing_turtle.goto(0, -480)
bg.tracer(1)

#Player_movement
def Controls_Up():
    crossing_turtle.seth(90)
    crossing_turtle.fd(20)
##def Controls_Down():
##    crossing_turtle.seth(-90)
##    crossing_turtle.fd(20)
##bg.onkey(Controls_Down, "Down")
##def Controls_Right():
##    crossing_turtle.seth(0)
##    crossing_turtle.fd(20)
##bg.onkey(Controls_Right, "Right")
##def Controls_Left():
##    crossing_turtle.seth(-180)
##    crossing_turtle.fd(20)
##bg.onkey(Controls_Left, "Left")

#Cars_movement
all_cars = []
game_on = True
while game_on:
    bg.listen()
    bg.onkey(Controls_Up, "Up")
    bg.tracer(0)
    cars = turtle.Turtle()
    x_axis = random.randint(700, 950)
    y_axis = random.randint(-400, 400)
    turtle.colormode(255)
    cars.fillcolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    cars.begin_fill()
    cars.pu()
    cars.goto(x_axis, y_axis)
    cars.shape("square")
    cars.shapesize(stretch_len = 5, stretch_wid = 3)
    all_cars.append(cars)
    for i in all_cars:
        i.fd(-100)
        if crossing_turtle.distance(i) <= 40:
            game_on = False
            text = turtle.Turtle()
            text.write("Game over" ,  False,  align = "center", font = ('Times new roman', 100, 'normal'))
    bg.tracer(1)
    time.sleep(0.1)
bg.exitonclick()
