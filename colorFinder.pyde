

# négyzetrácsban színek, egy kivételével mind ugyanolyan, ha rákattintasz az egyedire, akkor szintet lépsz. 
# Az egyedi szín egyre közelebb kerül a tömeg színhez


# TODO : négyzetek között üres hely, lkekerekített

# lvl 1 -> 3x3
# lvl 2 -> 4x4

# max: 15x15?

import random

level = 3
diff = 20

r = random.randint(diff,255-diff)
g = random.randint(diff,255-diff)
b = random.randint(diff,255-diff)

r2 = floor(r+random.randint(-diff,diff))
g2 = floor(g+random.randint(-diff,diff))
b2 = floor(b+random.randint(-diff,diff))

gridColor = color(r,g,b)
guessColor = color(r2,g2,b2)

w = 600
h = 600

unit = w/level

def setup():
    size(w,h)  
    global guessX, guessY
    guessX = random.randint(0,level-1)
    guessY = random.randint(0,level-1)

    background(gridColor)
    fill(guessColor)
    rect(guessX*unit,guessY*unit,unit,unit)
    
    for i in range(level+1):
        for j in range(level+1):
            line(w/level*i,0,w/level*i,h)
            line(0,h/level*j,w,h/level*j)
            
def draw():
    pass

            
def mouseClicked():
    global guessLocation, level, unit, gridColor, guessColor, r,g,b,r2,g2,b2, diff
    c = get(mouseX,mouseY)
    if c == guessColor:
        if level < 10:
            level += 1
        unit = w/level
        guessX = random.randint(0,level-1)
        guessY = random.randint(0,level-1)
        #print(r,g,b,'|',r2,g2,b2,'|', diff)
        
        if diff > 5:
            diff-= 1        
        r = random.randint(diff,255-diff)
        g = random.randint(diff,255-diff)
        b = random.randint(diff,255-diff)
        
        r2 = floor(r+random.randint(-diff,diff))
        g2 = floor(g+random.randint(-diff,diff))
        b2 = floor(b+random.randint(-diff,diff))
        
        gridColor = color(r,g,b)
        guessColor = color(r2,g2,b2)
        
        background(gridColor)
    
        fill(guessColor)
        rect(guessX*unit,guessY*unit,unit,unit)
        
        for i in range(level+1):
            for j in range(level+1):
                line(w/level*i,0,w/level*i,h)
                line(0,h/level*j,w,h/level*j)
