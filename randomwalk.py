# import turtle as t
# import random
# tim = t.Turtle()
# colors = ["brown", "red", "dark green", "dark magenta"]
# tim.pensize(10)
# tim.speed(speed="fastest")
# for _ in range(1, 150):
#     tim.color(random.choice(colors))
#     tim.forward(15)
#     tim.goto(random.randint(-150, 0), random.randint(0, 150))

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, g, b)

tim.pensize(10)
tim.speed(speed="fastest")
for _ in range(1, 150):
    tim.color(random_color())
    tim.forward(15)
    tim.goto(random.randint(-150, 0), random.randint(0, 150))

