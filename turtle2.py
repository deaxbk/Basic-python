Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Recangle():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

        
def circle():
    for i in range(12):
        tao.circle(60)
        tao.left(30)

        
def octagon():
    for i in range(8):
        tao.forward(60)
        tao.left(45)

        
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

    
circle()
Go(200,200)
Recangle()
Go(-200,0)
Go(-200,0)
Go(-200,0)
Go(-200,200)
octagon()
