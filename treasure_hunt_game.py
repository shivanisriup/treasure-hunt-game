import math
import turtle
import random

# Make a turtle on screen and change its shape to ’turtle’ and color to ‘green’.
t= turtle.Turtle()
t.shape("turtle")
t.color('green')

# Pick random X and Ys
treasure_x = random.randint(-100,100)
treasure_y = random.randint(-100,100)
print(treasure_x)
print(treasure_y)
gameover=False
current_x=int(input('Enter current guess X coordinate lies between -100 and 100'))
current_y=int(input('Enter current guess Y coordinate lies between -100 an 100'))
original_x=current_x
original_y=current_y
while gameover==False:
    try:
        current_x=int(input('Enter current guess X coordinate lies between -100 and 100'))
        current_y=int(input('Enter current guess Y coordinate lies between -100 an 100'))
        t.goto(current_x,current_y)
        originaldistance=math.sqrt(((original_x-treasure_x)**2)+((original_y-treasure_y)**2))
        currentdistance=math.sqrt(((current_x-treasure_x)**2)+((current_y-treasure_y)**2) )
        if currentdistance < originaldistance:
            t.color('orange')
            t.write('you are getting warmer',None, "center", "16pt bold")
        elif currentdistance>originaldistance:
            t.color('dark blue')
            t.write('you are getting colder',None, "center", "16pt bold")
    except:
        print ('Error, enter numeric input')
    if current_x==treasure_x and current_y==treasure_y:
            t.color('red')
            t.write('you won the game',None, "center", "16pt bold")
            gameover=True

