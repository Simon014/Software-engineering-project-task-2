"""
this is the main program. this DOES NOT have OOP principles, as that is demonstrated in the traploader.
This part handles the collisions and movement and map loading.
"""
import turtle
import traploader
traps = [] #to be used by the traploader
try : 
    from PIL import Image
except:
    from pil import Image
#DEBUG VARIABLES

COLCHECK = 0
TRAP = 0



#GAME VARIABLES
mp = 1
colmap = Image.open("levels\\" + str(mp) + "\\5kx5kc.png")

t = turtle.Turtle()
debug = turtle.Turtle()
debug.speed(0)
debug.forward(10)
debug.penup()
debug.color('red')
c = turtle.Turtle()
c.hideturtle()
c.speed(0)
c.penup()
t.speed(0)
t.penup()
b = turtle.Turtle()
b.color('blue')
b.penup()
b.forward(55)

turn = False
yv = 0
ya = 0 
x,y = b.xcor(), b.ycor()
sc = turtle.Screen()
#traps
t1 = traploader.trap_water(841,354, 'none', sc, 'blue',traps)
t2 = traploader.trap_water(857,167, 'none', sc, 'blue',traps)
t3 = traploader.trap_water(849,265, 'none', sc, 'blue',traps)
t4 = traploader.trap_water(849,216, 'none', sc, 'blue',traps)
t5 = traploader.trap_water(846,309, 'none', sc, 'blue',traps)
t6 = traploader.trap_water(857,112, 'none', sc, 'blue',traps)


print(traps)
car = sc.addshape(r"levels\\" + str(mp) + "\\car.gif")
t.shape(car)
sc.bgpic("levels\\" + str(mp) + "\\5kx5k.gif")
sc.screensize(5000,5000)
def d():
    global yv
    global turn
    t.right(10)
    t.forward(yv)
    turn = True
    scrl()
    colcheck()
    return
def a():
    global yv
    global turn
    t.left(10)
    t.forward(yv)
    turn = True
    scrl()
    colcheck()
    return
def j():
    global ya
    ya = 2
    return
def s():
    global ya
    ya = -2
    return
def stop(x,y):
    global yv
    yv = 0
    t.goto(0,0)
    return
def scrl():
    scl = sc.getcanvas()
    if sc.window_width() > 1000:
        scl.yview_moveto(0.42 - 0.0002 *t.ycor())
        scl.xview_moveto(0.35 + 0.0002 *t.xcor())
    else:
        scl.yview_moveto(0.435 - 0.0002 *t.ycor())
        scl.xview_moveto(0.43 + 0.0002 *t.xcor())
    return
def test(xt,yt):
    debug.goto(xt,yt)
def colcheck():
    global colmap
    global yv
    global COLCHECK
    if COLCHECK == 1:
        return
    xc = t.xcor()
    yc = t.ycor()
    xf = 2500 + xc #convert turtle position to pixel position
    yf = 2500 - yc
    xy = (xf,yf)
    r,g,b,a = colmap.getpixel(xy)
    if r == 255 and g == 0 and b == 0:
        print("collision")
        yv = 0
        stop("a variable","another variable")
    #run the trap list
    yv = t1.script(t, yv)
    yv = t2.script(t, yv)
    yv = t3.script(t, yv)
    yv = t4.script(t, yv)
    yv = t5.script(t, yv)
    yv = t6.script(t, yv)
    
def getpixel():
    x = debug.xcor()
    y = debug.ycor()
    print("pixel position relative to 0,0")
    print(f"{x},{y}")
    print("pixel position relative to background.")
    x = 2500 + x #convert turtle position to pixel position
    y = 2500 - y
    print(f"{x},{y}")

def debugger():
    global COLCHECK
    global TRAP
    inpt = input("==> ")
    while inpt != 'esc':
        if inpt == 'getpixel':
            getpixel()
        elif inpt == "DEBUG2POS":
            test(t.xcor(),t.ycor())
        elif inpt == "game variables":
            print(f"colcheck = {COLCHECK}")
            print(f"TRAP = {TRAP}")
            print("type in variable name to change")
            inpt2 = input("=> ")
            if inpt2 == "COLCHECK":
                COLCHECK = int(input("new state : "))
            elif inpt2 == "TRAP":
                TRAP = int(input("new state : "))
            print("variables saved.")
        inpt = input("==> ")
    return
                
    
colcheck()
sc.onkeypress(d,'d')
sc.onkeypress(a,'a')
sc.onkeypress(j,'w')
sc.onkeypress(s,'s')
sc.onkeypress(getpixel, '~')
sc.onkey(debugger,'*')
t.onclick(stop)
debug.ondrag(test)
sc.listen()
while True:
    t.forward(yv)
    yv += ya
    ya = 0
    scrl()
    turn = 0
    colcheck()
turtle.done()
