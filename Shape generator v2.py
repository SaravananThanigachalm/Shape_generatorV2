"""
Welcome to the Shape generator V1

@author: Saravanan T

last edited date - 3/7/2020
"""

import random
import turtle
import math

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.up()
t1.goto(0,250)
style1 = ('Arial', 24, 'italic')
t1.color("red")
t1.write('Welcome to Shape Generator V2', font=style1, align='center')
t1.hideturtle()
t2.up()
t2.goto(0,200)
style2 = ('Arial', 22)
t2.color("orange")
t2.write('By Saravanan T', font=style2, align='center')
t2.hideturtle()

cal1 = turtle.Turtle()
cal2 = turtle.Turtle()
cal3 = turtle.Turtle()
poly = turtle.Turtle()

class Polygon:
    color = ["red","yellow", "gold", "orange", "maroon", "violet", "magenta", "navy blue", "skyblue", "lightgreen", "green", "darkgreen", "brown", "gray"]
    picked_color = random.choice(color)
    poly = turtle.Turtle()
    cal1 = turtle.Turtle()
    cal2 = turtle.Turtle()
    

    def __init__(self, name, sides, length, color = picked_color, line_thickness = 5):
        self.name = name
        self.sides = sides
        self.length = length
        self.color = color
        self.line_thickness = line_thickness
        if(self.sides>2):
            self.interior = (self.sides - 2) * 180
            self.angles = self.interior / self.sides

    def calc(self):
        if (self.sides == 0):
            self.perimeter = round(2 * math.pi * self.length, 3)
            self.area = round(math.pi * self.length ** 2, 3)
        else:
            self.perimeter = round(self.length * self.sides, 3)
            self.apothem = self.length / ( 2 * math.tan( math.pi/self.sides ) )
            self.area = round((self.perimeter * self.apothem) / 2, 3)
                
        
    def draw(self):
        cal1.up()
        cal1.goto(-350,30)
        style3 = ('Arial', 20)
        cal1.color("blue")
        cal1.write("The perimeter of the given polygon is "+str(self.perimeter)+" units", font=style3, align='center')
        cal1.hideturtle()
        cal2.up()
        cal2.goto(-350,-10)
        style3 = ('Arial', 20)
        cal2.color("blue")
        cal2.write("The Area of the given polygon is "+str(self.area)+" units", font=style3, align='center')
        cal2.hideturtle()
        
        cal3.up()
        cal3.goto(-300,70)
        style3 = ('Arial', 20)
        cal3.color("navy blue")
        cal3.write(" Figure "+str(self.name), font=style3, align='center')
        cal3.hideturtle()


        poly.up()
        poly.goto(250,-200)
        poly.color(self.color)
        poly.pensize(self.line_thickness)
        poly.down()

        if(self.sides == 0):
            poly.circle(150)
        else:
            for j in range(self.sides):
                poly.forward(150)
                poly.left(180 - self.angles)
        poly.hideturtle()
        turtle.done()



x = str(input("Please specify name of the Polygon"))
y = int(input("Please specify the number of sides"))
# Please specify the number of sides as zero to create circles
z = int(input("Please specify the length of the side"))

x = Polygon(x, y, z)
x.calc()
x.draw()

""" Here it is the version 2 fully improved almost zero bugs  """

