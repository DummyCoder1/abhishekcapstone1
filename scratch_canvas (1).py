import random
import turtle

turtle.speed(0)

turtle.Screen().bgcolor("black")

def pen(colour):
    turtle.color(colour)  


    
def firework1(size):
    for num in range(20):
        turtle.forward(size)
        turtle.right(180-360/20)
        
firework1(20)

def move():
    turtle.penup()
    x=random.randint(-150,150)
    y=random.randint(-150,150)
    turtle.goto(x,y)
    turtle.pendown()

move()
pen('yellow')
firework1(30)
move()
pen('blue')
firework1(57)
move()
pen('purple')
firework1(80)
move()
pen('lightblue')
firework1(120)
move()
pen('gold')
firework1(150)
move()
pen('pink')
firework1(100)
move()
pen('orange')
firework1(54)
move()
pen('violet')
firework1(33)
move()
pen('green')
firework1(68)
pen('red')
move()
pen('white')
firework1(69)
move()
pen('pink')
firework1(72)
move()
pen('cyan')
firework1(51)
move()
pen('green')
firework1(169)
move()
pen('orange')
firework(65)
move()
pen('yellow')
firework(66)
