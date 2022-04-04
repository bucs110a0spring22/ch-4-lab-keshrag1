import turtle
import math
def drawSineCurve(dart):
  """
  Draws a sine curve from -360 to 360.
  args: dart (object) the thing that draws the sine curve
  returns: none
  """
  shape = input("Choose a shape?: ")
  color = input("Choose a color?: ")
  dart.shape(shape)
  dart.color(color)
  for i in range(-360,361,1):
    y_coordinate=math.sin(math.radians(i))
    dart.shape("turtle")
    dart.goto(i,y_coordinate)
  dart.up()

def setupWindow(wn):
  """
  changes the scale of the screen to represent the sine curve.
  args: wn (class) is the screen that turtle is on
  returns
  """
  wn.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(dart):
  """
  The function draws the x and y axis.
  args: dart (object) dart draws the axis
  returns: none
  """
  dart.goto(-360,0)
  dart.forward(720)
  dart.goto(0,-360)
  dart.left(90)
  dart.forward(720)


def drawCosineCurve(dart):
  """
  The function draws a cosine curve
  args: dart (object) the dart is the turtle that draws the cosinse curve
  """
  shape = input("Choose a shape?: ")
  color = input("Choose a color?: ")
  dart.shape(shape)
  dart.color(color)
  for i in range(-360,361,1):
    x_coordinate=i
    y_coordinate=math.cos(math.radians(i))
    dart.goto(x_coordinate,y_coordinate)
    dart.down()
  dart.up()

def drawTangentCurve(dart):
  """
  The function draws a tangent curve.
  args: dart (object) dart is the turtle that is drawing the tangent curve
  returns: none
  """
  shape = input("Choose a shape?: ")
  color = input("Choose a color?: ")
  dart.shape(shape)
  dart.color(color)
  for i in range(-360,361,1):
    x_coordinate=i
    y_coordinate=math.tan(math.radians(i))
    dart.goto(x_coordinate,y_coordinate)
    dart.down()

def midterm_function(para_1=0, para_2=0, para_3=0):
  """
  This function calculates the difference between the number of apples and bananas
  args: para_1(int), para_2(int), para_3(int) these calculate the number of apples and bananas
  returns: Kia has str(difference) more apples than bananas (str). Kia has str(difference) more bananas than apples (str), Kia has the same number of apples and apples(str). These return the difference in number of apples and bananas
  """
  num_apples = para_1*para_2
  num_bananas= para_2 * para_3
  if num_apples > num_bananas:
    difference = num_apples-num_bananas
    return "Kia has " + str(difference) + " more apples than bananas"
  elif num_bananas > num_apples:
    subtract = num_bananas - num_apples
    return "Kia has " + str(subtract) + " more bananas than apples"
  elif num_apples == num_bananas:
    return "Kia has the same number of apples and bananas"
  
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
    print(midterm_function(4,3,2))
    wn.exitonclick()
main()