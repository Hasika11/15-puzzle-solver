#!/usr/bin/env python
#PPROBLEM FORMULATION IN README
#TEAM MEMBERS
#Hasika Mahtta
#Ayesha Bhimdiwala
#Satendra Varma

# put your 15 puzzle solver here!
from heapq import heappush,heappop
import copy
import timeit
import sys
start=timeit.default_timer()
def zero_cord(b) :
    for i in range (0,4) :
            for j in range (0,4) :
                if b[i][j]==0 :
                    return [i,j]

def permutation_check(s):
    sd=[]
    rcnt=4
    zero_row=0
    xcord=0
    for li in  s :
        if 0 in li :
            x=xcord
            zero_row=rcnt
            ycord=0
            for b in li :
                if b==0 :
                    y=ycord
                    break
                else :
                    ycord+=1
        xcord+=1
        rcnt-=1
        sd=sd+li
    cnt =0
    for i in range(0,len(sd)-1) :
        for j in range(i+1,len(sd)) :
            if sd[i] != 0 and sd[i]!=1 and sd[j]!=0 :
                if sd[i] > sd[j] :
                    cnt+=1
    result=[x,y]
    if (cnt+zero_row)%2==0:
        result.append(False)
        return result
    else :
        result.append(True)
        return result


def successors(board):
    s=[]
    result=permutation_check(board)
    if result[2] == False:
        return s
    #cord=zero_cord(board)
    r=result[0]
    c=result[1]
    moves=[]
    boardup = copy.deepcopy(board)
    if r > 0 :
        boardup[r][c],boardup[r-1][c]=boardup[r-1][c],boardup[r][c]
        s.append(boardup)
        moves.append('D1'+(str)(c+1))
        boardup2 = copy.deepcopy(boardup)
        if r > 1 :
            boardup2[r-1][c],boardup2[r-2][c]=boardup2[r-2][c],boardup2[r-1][c]
            s.append(boardup2)
            moves.append('D2'+(str)(c+1))
            boardup3=copy.deepcopy(boardup2)
            if r > 2 :
                boardup3[r - 3][c], boardup3[r - 2][c] = boardup3[r - 2][c], boardup3[r - 3][c]
                s.append(boardup3)
                moves.append('D3'+(str)(c+1))
    boarddown = copy.deepcopy(board)
    if r < 3 :
        boarddown[r][c],boarddown[r+1][c]=boarddown[r+1][c],boarddown[r][c]
        s.append(boarddown)
        boarddown2=copy.deepcopy(boarddown)
        moves.append('U1'+(str)(c+1))
        if r < 2 :
            boarddown2[r +1][c], boarddown2[r + 2][c] = boarddown2[r + 2][c], boarddown2[r+1][c]
            s.append(boarddown2)
            boarddown3 = copy.deepcopy(boarddown2)
            moves.append('U2'+(str)(c+1))
            if r < 1 :
                boarddown3[r + 2][c], boarddown3[r + 3][c] = boarddown3[r + 3][c], boarddown3[r + 2][c]
                s.append(boarddown3)
                moves.append('U3'+(str)(c+1))
    boardleft = copy.deepcopy(board)
    if c > 0 :
        boardleft[r][c],boardleft[r][c-1]=boardleft[r][c-1],boardleft[r][c]
        s.append(boardleft)
        moves.append('R1'+(str)(r+1))
        boardleft2=copy.deepcopy(boardleft)
        if c >  1:
            boardleft2[r][c-1], boardleft2[r][c - 2] = boardleft2[r][c - 2], boardleft2[r][c-1]
            s.append(boardleft2)
            moves.append('R2'+(str)(r+1))
            boardleft3 = copy.deepcopy(boardleft2)
            if c>2:
                boardleft3[r][c-3], boardleft3[r][c - 2] = boardleft3[r][c - 2], boardleft3[r][c-3]
                s.append(boardleft3)
                moves.append('R3'+(str)(r+1))
    boardright = copy.deepcopy(board)
    if c<3 :
        boardright[r][c],boardright[r][c+1]=boardright[r][c+1],boardright[r][c]
        s.append(boardright)
        boardright2=copy.deepcopy(boardright)
        moves.append('L1'+(str)(r+1))
        if c<1:
            boardright2[r][c+1], boardright2[r][c + 2] = boardright2[r][c + 2], boardright2[r][c+1]
            s.append(boardright2)
            moves.append('L2'+(str)(r+1))
            boardright3 = copy.deepcopy(boardright2)
            if c<2:
                boardright3[r][c+2], boardright3[r][c + 3] = boardright3[r][c + 3], boardright3[r][c+2]
                s.append(boardright3)
                moves.append('L3'+(str)(r+1))
    re=[s,moves]
    return re


#Number_misplaces tiles(s)
def heuristic_calc(s):
    count = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if x[i][j]!= s[i][j] and s[i][j]!= 0 :
                count = count + 1
    return count


actual_pos={1:(0,0),2:(0,1),3:(0,2),4:(0,3),5:(1,0),6:(1,1),7:(1,2),8:(1,3),9:(2,0),10:(2,1),11:(2,2),12:(2,3),13:(3,0),14:(3,1),15:(3,2),0:(3,3)}
def manhattan_calc(s):
    global dist
    final_dist = 0
    for i in range(0, 4):
        for j in range(0, 4):
            val = s[i][j]
            if val!=0 :
                temp=actual_pos[val]
                k=temp[0]
                l=temp[1]
                dist = abs(k-i)+abs(l-j)
                final_dist += dist
    return float(final_dist/3.00)
    
def is_goal(s):
    if s == x:
       return True
    else :
        return False

def solve(st):
    Fringe = []
    visited=[]
    heappush(Fringe,(0,st,0,''))
    visited.append(st)
    while Fringe[0]!=IndexError:
        step=Fringe[0][2]
        curmov=Fringe[0][3]
        re=successors(heappop(Fringe)[1])
        succ=re[0]
        mov=re[1]
        if len(succ)!=0 :
            step+=1
            count=0
            for s1 in succ:
                if is_goal(s1) :
                    print step
                    return curmov+mov[count]+" "
                if s1 not in visited :
                    visited.append(s1)
                    hs2 = manhattan_calc(s1)
                    heappush(Fringe,(hs2+step,s1,step,curmov+mov[count]+" "))
                count+=1

text_file_name=sys.argv[1]

f=open(text_file_name,"r")
lines=f.read().splitlines()
input=[]
for x in lines :
    temp=x.split(  )
    temp1= list(map(int, temp))
    input.append(temp1)
f.close()
x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

print solve(input)
