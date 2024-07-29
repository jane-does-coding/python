import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_segments = []

def create_segment():
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    return segment

for _ in range(3):
    segment = create_segment()
    segment.goto(-20 * _, 0)
    snake_segments.append(segment)

def move():
    for i in range(len(snake_segments) - 1, 0, -1):
        x = snake_segments[i - 1].xcor()
        y = snake_segments[i - 1].ycor()
        snake_segments[i].goto(x, y)
    snake_segments[0].forward(20)

def go_up():
    if snake_segments[0].heading() != 270:
        snake_segments[0].setheading(90)

def go_down():
    if snake_segments[0].heading() != 90:
        snake_segments[0].setheading(270)

def go_left():
    if snake_segments[0].heading() != 0:
        snake_segments[0].setheading(180)

def go_right():
    if snake_segments[0].heading() != 180:
        snake_segments[0].setheading(0)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

while True:
    screen.update()
    move()

screen.exitonclick()
