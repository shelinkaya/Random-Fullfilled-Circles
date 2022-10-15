from turtle import Screen, Turtle
from random import randint

FIBER_RADIUS = 25
FIBER_NUMBER = 100
CURSOR_SIZE = 20

def fiber_circle(fiber):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    x = randint(FIBER_RADIUS - width//2, width//2 - FIBER_RADIUS)
    y = randint(FIBER_RADIUS - height//2, height//2 - FIBER_RADIUS)

    fiber.color(r, g, b)
    fiber.goto(x, y)
    fiber.dot(FIBER_RADIUS * 2)  # dot() takes a diameter

screen = Screen()
screen.colormode(255)

width, height = screen.window_width(), screen.window_height()

fiber = Turtle()
fiber.hideturtle()
fiber.speed("fastest")
fiber.penup()

for _ in range(FIBER_NUMBER):
    fiber_circle(fiber)

screen.exitonclick()
