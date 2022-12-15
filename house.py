from base64 import standard_b64encode
import turtle

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Turtle House')

roof = turtle.Turtle()
roof.color('black', 'red')

roof.begin_fill()
for i in range(3):
    roof.forward(200)
    roof.left(120)
roof.end_fill()

roof.hideturtle()

house = turtle.Turtle()
house.color('black', 'yellow')

house.begin_fill()
house.right(90)
house.forward(200)
house.left(90)
house.forward(200)
house.left(90)
house.forward(200)
house.left(90)
house.end_fill()

house.hideturtle()

door = turtle.Turtle()
door.color('black', 'blue')

door.penup()
door.goto(80, -200)
door.pendown()

door.begin_fill()
door.left(90)
door.forward(100)
door.right(90)
door.forward(40)
door.right(90)
door.forward(100)
door.end_fill()

wn = turtle.Turtle()
wn.color('black', 'green')

wn.penup()
wn.goto(30, -150)
wn.pendown()

wn.begin_fill()
for i in range(4):
    wn.forward(30)
    wn.left(90)
wn.end_fill()


wn.penup()
wn.goto(140, -150)
wn.pendown()

wn.begin_fill()
for i in range(4):
    wn.forward(30)
    wn.left(90)
wn.end_fill()

tu = turtle.Turtle()
tu.color('green')
tu.penup()
tu.goto(-300, -100)
tu.pendown()

tu.left(90)
tu.backward(80)
tu.speed(200)
tu.shape('turtle')


def tree(i):
    if i < 10:
        return
    else:
        tu.forward(i)
        tu.color('orange')

        tu.circle(2)
        tu.color('brown')

        tu.left(30)
        tree(3 * i/4)
        tu.right(60)
        tree(3 * i/4)
        tu.left(30)
        tu.backward(i)


tree(80)

moon = turtle.Turtle()
moon.color('white', 'white')
moon.speed(0)

moon.penup()
moon.goto(400, 300)
moon.pendown()

moon.begin_fill()
for i in range(360):
    moon.forward(1)
    moon.right(1)
moon.end_fill()


star = turtle.Turtle()
star.color('white', 'white')

star.penup()
star.goto(-420, 220)
star.pendown()

star.begin_fill()
for i in range(12):
    star.forward(30)
    star.right(150)
star.end_fill()

turtle.done()
