from tkinter import *
import random

def next_turn(row, column):        #we define a function named "next_turn"
    
    global player       #access to our player

#we check to see if the button that we click on is empty:

    if buttons[row][column]['text'] == "" and check_winner() is False:

       if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:  
                 player = players[1]
                 label.config(text=(players[1]+" turn"))       #if there is no winner, then we are going to swap players
                  
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

       else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

def check_winner():     #we define a function named "check_winner"
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":     #if all of these buttons are the  same and they are not equal to an empty space
            return True     #that means that somebody won
    
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":     #if all of these buttons are the  same and they are not equal to an empty space
            return True     
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "": 
            return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            return True
    
    elif empty_spaces() is False:
        
        for row in range(3):
            for column in range(3):
             return "Tie"
    
    else:
        return False


def empty_spaces():     #we define a function named "empty_spaces" to check if there are any empty spaces left
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
    
    if spaces == 0:  #spaces remaining is equal to zero, that means we will return false, so there are no spaces left
        return False
    else:
        return True

                
def new_game():         #we define a function named "new_game" that will launch a new game for us
    
    global player

    player =random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")  #hexdecimal color


window = Tk()           #we create a window
window.title("Tic-Tac-Toe")         #we set the name
players = ["x","o"]        #we create a list of players
player = random.choice(players)     #we select a random player from the list of players to begin 

#we create a 2d list of buttons named "buttons":
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]      

label = Label(text= player + " turn", font=('consolas',40))     #we need a label label to display whose turn it is
label.pack(side="top")    

#we create a reset button:
reset_button = Button(text="restart", font=('consolas',20), command=new_game)       #when we click on this button it's going to call this new game function for us
reset_button.pack(side="top")

frame = Frame(window)       #we are going to place these all within a frame
frame.pack()

#we create de rows and columns for the game
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2, command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
window.mainloop()       #a small window should appear
