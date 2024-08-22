import turtle
try :
    from PIL import Image
except :
    from pil import Image
class trap_water:
    def __init__(self, x, y, sprite, screen, color, traps):
        """
        TRAP LOADER INITIATOR FUNCTION

        x -> x cordinate of trap
        y -> y cordinate of trap
        screen -> screen object
        """
        
        self.x = x
        self.y = y
        self.sprite = sprite
        self = turtle.Turtle()
        #initalise trap pos
        self.color(color)
        self.speed(0)
        self.penup()
        self.goto(x,y)
        loc = str(x) + ' ' + str(y)
        traps.append(loc)
        
    def script(self,t,yv):
        x = t.xcor()
        y = t.ycor()
        if abs(x - self.x) < 48:
            if abs(y -  self.y) < 48:
                if yv > 0:
                    yv = 10
                elif yv < 0:
                    yv = -10
                else :
                    yv = 0
        return yv
        
        """
        TRAP SCRIPT.

        OVERRIDE THIS FUNCTION AND PUT TRAP CODE IN THE OBJECT.
        """
        
        pass
