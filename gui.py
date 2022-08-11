from tkinter import * #Tk, Label, Button, NORMAL, DISABLED, ImagePhoto
from utility import *
from random import choice

def place(x): # since i am using the older gui which was based on a 3*3 matrix
	if x==1:
		return [1,1]
	if x==2:
		return [1,2]
	if x==3:
		return [1,3]
	if x==4:
		return [2,1]
	if x==5:
		return [2,2]
	if x==6:
		return [2,3]
	if x==7:
		return [3,1]
	if x==8:
		return [3,2]
	if x==9:
		return [3,3]

game = ttt()
root = Tk()
gameType='Single Player'

icon = PhotoImage(file = "images/table.png")
circle = PhotoImage(file ="images/circle.png")
cross = PhotoImage(file ="images/cross.png")
bg = PhotoImage(file="images/bg.png")

root.iconphoto(False, icon)
root.title("TicTacToe")
root.geometry("210x270")

toss = choice(['o','x'])
Label(root,text=f"{toss.upper()} first",font=('Castellar',10)).grid(row=4,column=3)

def checkGame():
        if game.status()==False:
            if game.move<10:
                val = str(game.winner).upper()+" won"
                Label(root,text=val,font=('Castellar',10)).grid(row=4,column=1)
                Label(root,text=f"           ",font=('Castellar',10)).grid(row=4,column=3)
            for i in range(3):
                for j in range(3):
                    buttons[i][j]['state']=DISABLED
                    
def movePlayer(x,player='o'):
    game.mark(player,x)
    if player!='o':
            buttons[place(x)[0]-1][place(x)[1]-1]['state']=DISABLED
            buttons[place(x)[0]-1][place(x)[1]-1]['bg']='red'
            buttons[place(x)[0]-1][place(x)[1]-1]['image']=cross
            Label(root,text=f"O's move",font=('Castellar',8)).grid(row=4,column=3)
            checkGame()
    else:
            buttons[place(x)[0]-1][place(x)[1]-1]['state']=DISABLED
            buttons[place(x)[0]-1][place(x)[1]-1]['bg']='blue'
            buttons[place(x)[0]-1][place(x)[1]-1]['image']=circle
            if gameType=='2Player':
                Label(root,text=f"X's move",font=('Castellar',8)).grid(row=4,column=3)
            checkGame()

def moveOpponent():
    if game.status()==True and game.isMoveLeft()==True:
        move = game.findBestMove()+1
        game.mark('x',move)
        move = place(move)
        buttons[move[0]-1][move[1]-1]['state']=DISABLED
        buttons[move[0]-1][move[1]-1]['bg']='red'
        buttons[move[0]-1][move[1]-1]['image']=cross
        if game.move!=1:
                Label(root,text=f"           ",font=('Castellar',10)).grid(row=4,column=3)
        checkGame()
    else:
        if game.move<9:
            val = str(game.winner).upper()+" won"
            Label(root,text=val,font=('Castellar',10)).grid(row=4,column=1)
        
        for i in range(3):
            for j in range(3):
                buttons[i][j]['state']=DISABLED

def makeMove(pos):
    if gameType=='2Player':
        if game.move%2==0:
                movePlayer(pos,player=toss)
        else:
                player = 'xo'.replace(toss,'')
                movePlayer(pos,player=player)
    else:
        movePlayer(pos)
        moveOpponent()

def reset_button(x,y):
    buttons[x][y]['state']=NORMAL
    buttons[x][y]['bg']='#e464f5'
    buttons[x][y]['image']=bg
    Label(root,text="          ",font=('Castellar',10)).grid(row=4,column=1)

def reset_game():
    global toss
    toss = choice(['o','x'])
    for i in range(3):
        for j in range(3):
            reset_button(i,j)
    game.reset()
    game.winner=None
    Label(root,text=f"{toss.upper()} first",font=('Castellar',10)).grid(row=4,column=3)
    if toss=='x' and gameType=='Single Player':
        moveOpponent()

def play():
        global gameType
        gameType='Single Player'
        reset_game()
def play1():
        global gameType
        gameType='2Player'
        reset_game()

menubar = Menu(root)
root.config(menu=menubar)
# create a menu
file_menu = Menu(menubar)
file_menu = Menu(menubar, tearoff=False)
# add a menu item to the menu
file_menu.add_command(label='Single Player',command=play)
file_menu.add_command(label='2Player',command=play1)
# add the File menu to the menubar
menubar.add_cascade(label="Settings",menu=file_menu)


box1 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(1),fg="black",bg="#e464f5")
box1.grid(row=1,column=1)
box2 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(2),fg="black",bg="#e464f5")
box2.grid(row=1,column=2)
box3 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(3),fg="black",bg="#e464f5")
box3.grid(row=1,column=3)


box4 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(4),fg="black",bg="#e464f5")
box4.grid(row=2,column=1)
box5 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(5),fg="black",bg="#e464f5")
box5.grid(row=2,column=2)
box6 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(6),fg="black",bg="#e464f5")
box6.grid(row=2,column=3)

box7 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(7),fg="black",bg="#e464f5")
box7.grid(row=3,column=1)
box8 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(8),fg="black",bg="#e464f5")
box8.grid(row=3,column=2)
box9 = Button(root,image=bg,padx=20,pady=10,command=lambda : makeMove(9),fg="black",bg="#e464f5")
box9.grid(row=3,column=3)

buttons = [[box1,box2,box3],[box4,box5,box6],[box7,box8,box9]]  
root.resizable(False,False)
reset = Button(root,text="Reset",command=reset_game,fg="green",bg="white",font=("Algerian",13)).grid(row=4,column=2)
if toss=='x' and gameType=='Single Player':
        moveOpponent()

root.mainloop()
