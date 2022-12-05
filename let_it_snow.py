import random
import turtle
import numpy as np



def main(speed=0, bg_color="pink"):
    # create Turtle object
    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()
    
    # set speed to 'fastest = 0'
    myTurtle.speed(speed)
    # change background color
    turtle_screen.bgcolor(bg_color)
    sfcolor = ["white", "red","orange","brown","yellow","blue", "purple", "grey", "magenta", "black", "cyan", "grey"]
  
 
    """TODO: define different colors here"""


    for _ in range(11):
        # define some params
        size = 15
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]

        """TODO: set snowflake color here (one of the colors defined above)"""

        # Go to the start position of the snowflake
        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()
        myTurtle.color(random.choice(sfcolor))

        # draw the snowflake
        for _ in range(11):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)


def snowflake_branch(size, myTurtle):
    # This function draws one branch of the snowflake.
    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)


if __name__ == "__main__":
    main()
