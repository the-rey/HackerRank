#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    p = grid.index("p")
    m = grid.index("m")
     
    #div 
    ym,xm = divmod(m,n) #4,3 -> 1,1
    yp,xp = divmod(p,n)  #6,3 -> 2,0
    
    diff_x = xp-xm
    diff_y = yp-ym
    
    while diff_x != 0:
        if diff_x > 0:
            print("RIGHT")
            diff_x -= 1
        else:
            print("LEFT")
            diff_x += 1
            
    while diff_y != 0:
        if diff_y > 0:
            print("DOWN")
            diff_y -= 1
        else:
            print("UP")
            diff_y += 1

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.extend(list(input().strip()))
displayPathtoPrincess(m,grid)