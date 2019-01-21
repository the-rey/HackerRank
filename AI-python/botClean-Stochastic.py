#!/usr/bin/python
import math
# Head ends here

def diff(a, b):
    return (max(a-b,b-a))

def euclid(x1,y1,x2,y2):
    return math.sqrt((diff(x2,x1)*(diff(x2,x1)) + ((diff(y2,y1)*(diff(y2,y1))))))

def next_move(posr, posc, board):
    eu_diff = 9999
    xd = -1
    yd = -1
    for i in range(posr,(5+posr)): # 4 , 9
        
        
        for j in range(posc,5+posc):
            if board[i%5][j%5] == 'd':
                if euclid(j%5,i%5,posc,posr) < eu_diff:
                    xd = j%5
                    yd = i%5
                    eu_diff = euclid(j%5,i%5,posc,posr)

        # if xd > -1:
        #     yd = i%5
    

    diff_x = xd-posc
    diff_y = yd-posr

    
    if diff_x == 0 and diff_y == 0:
        print("CLEAN")
        return

    if diff_x > 0:
        print("RIGHT")
        diff_x -= 1
        return
    elif diff_x < 0:
        print("LEFT")
        diff_x += 1
        return
            
    if diff_y > 0:
        print("DOWN")
        diff_y -= 1
        return
    elif diff_y < 0:
        print("UP")
        diff_y += 1
        return
        

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)