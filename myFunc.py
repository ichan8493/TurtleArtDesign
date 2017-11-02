from random import randint

def petal(t):
    for times in range(20):
        t.color(50+times*10,0,0)
        t.begin_fill()
        t.circle(10+times*2)
        t.penup()
        t.forward(20)
        t.left(4)
        t.pendown()
        t.end_fill()

def petal2(t):
    for times in range(20):
        t.color(0,50+times*10,0)
        t.begin_fill()
        t.circle(10+times*2)
        t.penup()
        t.forward(20)
        t.left(4)
        t.pendown()
        t.end_fill()

def petal3(t):
    for times in range(20):
        t.color(0,0,50+times*10)
        t.begin_fill()
        t.circle(10+times*2)
        t.penup()
        t.forward(20)
        t.left(4)
        t.pendown()
        t.end_fill()

def blade(t):
    for times in range(20):
        t.color(0,50+times*10,50+times*10)
        t.begin_fill()
        polygon(t,10+times*2,3)
        t.penup()
        t.forward(20+times)
        t.left(4)
        t.pendown()
        t.end_fill()

def blade2(t):
    for times in range(20):
        t.color(50+times*10,50+times*10,0)
        t.begin_fill()
        polygon(t,10+times*2,3)
        t.penup()
        t.forward(20+times)
        t.left(4)
        t.pendown()
        t.end_fill()

def blade3(t):
    for times in range(20):
        t.color(50+times*10,0,50+times*10)
        t.begin_fill()
        polygon(t,10+times*2,3)
        t.penup()
        t.forward(20+times)
        t.left(4)
        t.pendown()
        t.end_fill()


def flowerp4(t):
    for times in range(4):
        blade(t)
        move(t,-30,10)
        t.left(32)
        blade2(t)
        move(t,-30,10)
        t.left(32)
        blade3(t)
        move(t,-30,10)
        t.left(32)
        
def flowerp1(t):
    for times in range(20):
        t.color(255,53,51)
        t.begin_fill()
        polygon(t,200,5)
        t.left(18)
        t.end_fill()

def flowerp2(t):
    t.color(255,255,51)
    t.begin_fill()
    t.circle(170)
    t.end_fill()

def flowerp3(t):
    for times in range(2):
        petal(t)
        t.left(36)
        petal2(t)
        t.left(36)
        petal3(t)
        t.left(36)

def flowerp4(t):
    for times in range(4):
        blade(t)
        move(t,-30,10)
        t.left(32)
        blade2(t)
        move(t,-30,10)
        t.left(32)
        blade3(t)
        move(t,-30,10)
        t.left(32)

def star(t):
     for times in range(5):
        t.forward(25)
        t.right(144)

def star2(t):
    for times in range(10):
        polygon(t,15,4)
        t.left(36)

def star3(t):
    for times in range(4):
        polygon(t,15,3)
        t.right(90)

def randStar(t):
    for times in range(25):
        x=randint(-600,600)
        y=randint(-600,600)
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        t.color(red,green,blue)
        move(t,x,y)
        t.begin_fill()
        star(t)
        t.end_fill()

def randStar2(t):
    for times in range(25):
        x=randint(-600,600)
        y=randint(-600,600)
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        t.color(red,green,blue)
        move(t,x,y)
        t.begin_fill()
        star2(t)
        t.end_fill()

def randStar3(t):
    for times in range(25):
        x=randint(-600,600)
        y=randint(-600,600)
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        t.color(red,green,blue)
        move(t,x,y)
        t.begin_fill()
        star3(t)
        t.end_fill()

def randomStars(t):
    randStar(t)
    randStar2(t)
    randStar3(t)


def polygon(t,distance,side):
    angle=360/side
    t.begin_fill()
    for times in range(side):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def move(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()




