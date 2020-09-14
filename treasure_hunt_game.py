import math
import turtle
import random
#from animations import congratulate
# Make a turtle on screen and change its shape to ’turtle’ and color to ‘green’.
t= turtle.Turtle()
t.shape("turtle")
t.color('green')# Pick random X and Ystreasure_x = random.randint(-100,100)treasure_y = random.randint(-100,100)print(treasure_x)print(treasure_y)
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
            print('you are getting warmer')
        elif currentdistance>originaldistance:
            print('you are getting colder')
        elif currentdistance == originaldistance:
            print('you are trying in wrong direction')
    except:
        print ('Error, enter numeric input')
    if current_x==treasure_x and current_y==treasure_y:
            print('you won the game')
            gameover=True
