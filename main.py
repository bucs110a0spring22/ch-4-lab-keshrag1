import turtle
import math
def drawSineCurve(dart):
  for i in range(-360,361,1):
    y=math.sin(math.radians(i))
    dart.shape("turtle")
    dart.goto(i,y)

def setupWindow(wn):
  wn.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(dart):
  turtle.setworldcoordinates(-360, -1, 360, 1)

def drawSineCurve(dart):
  for i in range(-360,361,1):
    x_coordinate=i
    y_coordinate=math.sin(math.radians(i))
    dart.shape("turtle")
    dart.goto(x_coordinate,y_coordinate)
  dart.up()

def drawCosineCurve(dart):
  for i in range(-360,361,1):
    x_coordinate=i
    y_coordinate=math.cos(math.radians(i))
    dart.goto(x_coordinate,y_coordinate)
    dart.down()
  dart.up()

def drawTangentCurve(dart):
  for i in range(-360,361,1):
    x_coordinate=i
    y_coordinate=math.tan(math.radians(i))
    dart.goto(x_coordinate,y_coordinate)
    dart.down()
  
  





##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
