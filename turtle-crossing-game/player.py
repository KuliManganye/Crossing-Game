from turtle import Turtle

# create a turtle player that starts at the bottom of the screen and listens for the "UP" keypress
# to move he turtle north

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # Creating the turtle player
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    # creating a move up function so the turtle can move up a distance of 10 pixels everytime
    # a player presses the "Up key"
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
