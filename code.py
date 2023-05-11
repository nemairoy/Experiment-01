import turtle

# Create the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle to draw with
t = turtle.Turtle()
t.speed(0)
t.penup()

# Set the starting position of the turtle
x = -300
y = 200
t.setpos(x, y)

# Create a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw the rainbow
for i in range(350):
    t.pendown()
    t.pensize(3)
    t.color(colors[i%7])
    t.circle(2*i)
    t.penup()
    t.backward(2)
    t.right(1)

# Hide the turtle
t.hideturtle()

# Keep the turtle window open until manually closed
turtle.done()



