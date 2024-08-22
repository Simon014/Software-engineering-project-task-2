#collision checker
def colcheck(colmap, yv, c,t):
    c.goto(t.xcor(),t.ycor())
    c.setheading(t.heading())
    c.forward(10)
    xc = c.xcor()
    yc = c.ycor()
    xf = 2500 + xc #convert turtle position to pixel position
    yf = 2500 - yc
    xy = (xf,yf)
    r,g,b,a = colmap.getpixel(xy)
    if r == 255 and g == 0 and b == 0:
        print("collision")
        yv = 0
    return yv
