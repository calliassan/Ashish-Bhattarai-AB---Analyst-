import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
def draw_spirograph(size):
    for i in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100, extent=None, steps=None)
        tim.setheading(tim.heading() + 5)
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()