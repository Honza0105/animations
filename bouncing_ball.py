from tkinter import *
import random
import time

heightCanvas = 400
widthCanvas = 500
g = 1
t = 0

####resolution of screen
##radius = 20
###radius of ball
##height_ab_gr = 300
###how is the ball high above ground in pixels


tk = Tk()
canvas = Canvas(tk, width = widthCanvas, height = heightCanvas)
tk.title('Bouncing ball')
canvas.pack()

#ball = canvas.creat_oval (10, heightCanvas - widthCanvas,
ball = canvas.create_oval(10 ,10 ,60 ,60 , fill='orange')

xspeed = 0
#speed in x direction
yspeed = 0
#speed in y direction
xaxcel = 0
#axceleration in x direction
yaxcel = g

yspeed_Sum = yspeed + 0
kinYSpeed = 0
kinXSpeed = 0
xspeed_Sum = xspeed
bounce = False

#axceleration in y direction
below = True
while True:
    #canvas.move(ball, xspeed_Sum, yspeed_Sum)
    pos = canvas.coords(ball)
    tk.update()
    if pos[3] >= heightCanvas:
        canvas.move(ball ,0, heightCanvas - pos[3]-30)
        #print(heightCanvas - pos[3])
##        saved_time = t
        t = 0
        kinYSpeed = -yspeed
        yspeed = 0
        time.sleep(1)
        bounce = True

    if abs(kinYSpeed + yspeed) < 10 and bounce == True:
        kinYSpeed = 0
        yspeed = 0
        t = 0
        bounce = False
    t += 1
    xspeed = xaxcel * t
    yspeed = yaxcel * t
    xspeed_Sum = xspeed + kinXSpeed
    yspeed_Sum = yspeed + kinYSpeed
    #print(abs(kinYSpeed - yspeed))




    canvas.move(ball, xspeed_Sum, yspeed_Sum)
    pos = canvas.coords(ball)

    time.sleep(1/30)
##    print('kinYSpeed', kinYSpeed, 'yspeed', yspeed)
##    print('yspeed', yspeed,'t' ,t,'pos[3]',
##          pos[3],'yspeed_Sum', yspeed_Sum,
##          'kinYSpeed', kinYSpeed, 'yspeed', yspeed)


tk.mainloop()
