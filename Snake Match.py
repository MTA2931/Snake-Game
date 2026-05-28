

#  -=-=-=-=-=-  SETUP MADULE  -=-=-=-=-=-  #
import turtle
import time
import random
import winsound







## -=-=-=-=-=-=-=-=-=-=-=- ##
## -=-=-=-=-=-=-=-=-=-=-=- ##
winsound.Beep(600,300)
delay = 0.1
score = 0
wn = turtle.Screen()
wn.title('Snake Match')
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)

### -=-=-=-=-=-=-=-=-=-=-=- ###
###          HEAD           ###
### -=-=-=-=-=-=-=-=-=-=-=- ###
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'


### -=-=-=-=-=-=-=-=-=-=-=- ###
###          FOOD           ###
### -=-=-=-=-=-=-=-=-=-=-=- ###
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)


segments = []


### -=-=-=-=-=-=-=-=-=-=-=- ###
###          MOVE           ###
### -=-=-=-=-=-=-=-=-=-=-=- ###
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'



def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_right, 'd')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_down, 's')


### -=-=-=-=-=-=-=-=-=-=-=- ###
###       GAME LOOP         ###
### -=-=-=-=-=-=-=-=-=-=-=- ###
while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('black')
        new_segment.penup()
        segments.append(new_segment)
        score = score+10
        print(score)

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            score = 0
            x = random.randint(-290,290)
            y = random.randint(-290,290)
            food.goto(x,y)


    time.sleep(delay)


#  -=-=-=-=-=-  RUN  -=-=-=-=-=-  #
wn.mainloop()

