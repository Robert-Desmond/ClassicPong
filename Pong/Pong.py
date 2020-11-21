import turtle
import winsound

# Scoring system
score1 = 0
score2 = 0

# Screen Setup
window = turtle.Screen()
window.title("Turtle Pong by Robert Desmond")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Left Paddle
lPaddle = turtle.Turtle()
lPaddle.speed(0)
lPaddle.shape("square")
lPaddle.color("white")
lPaddle.shapesize(stretch_wid=5, stretch_len=1)
lPaddle.penup()
lPaddle.goto(-350, 0)

# Right Paddle
rPaddle = turtle.Turtle()
rPaddle.speed(0)
rPaddle.shape("square")
rPaddle.color("white")
rPaddle.shapesize(stretch_wid=5, stretch_len=1)
rPaddle.penup()
rPaddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0  :  0", align = "center", font = ("Consolas", 24, "normal"))

## Functions
# Left paddle functions
def left_paddle_up():
    y = lPaddle.ycor()
    y += 40
    lPaddle.sety(y)

def left_paddle_down():
    y = lPaddle.ycor()
    y -= 40
    lPaddle.sety(y)

# Right paddle functions
def right_paddle_up():
    y = rPaddle.ycor()
    y += 40
    rPaddle.sety(y)

def right_paddle_down():
    y = rPaddle.ycor()
    y -= 40
    rPaddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() <= -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("{}  :  {}".format(score1, score2), align="center", font=("Consolas", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("{}  :  {}".format(score1, score2), align="center", font=("Consolas", 24, "normal"))

    # Paddle and ball check/collisions
    if (330 < ball.xcor() < 340) and (rPaddle.ycor() + 50 > ball.ycor() > rPaddle.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-330 > ball.xcor() > -340) and (lPaddle.ycor() + 50 > ball.ycor() > lPaddle.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddles stay on screen
    if lPaddle.ycor() > 245:
        lPaddle.sety(245)
    if lPaddle.ycor() <-240:
        lPaddle.sety(-240)

    if rPaddle.ycor() > 245:
        rPaddle.sety(245)
    if rPaddle.ycor() < -240:
        rPaddle.sety(-240)