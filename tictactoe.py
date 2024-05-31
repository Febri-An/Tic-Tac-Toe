import random
import time

def show_board(starting_game=False):
    if starting_game:
        print(" | ".join(A) + "  -> a0, a1, a2")
        print("---------")
        print(" | ".join(B) + "  -> b0, b1, b2")
        print("---------")
        print(" | ".join(C) + "  -> c0, c1, c2")
    else:
        print(" | ".join(A))
        print("---------")
        print(" | ".join(B))
        print("---------")
        print(" | ".join(C))

def check_and_mark(loc, symbol):
    if loc[0] == "A":
        if A[int(loc[1])] == " ":
            A[int(loc[1])] = symbol
            return True
        
    elif loc[0] == "B":
        if B[int(loc[1])] == " ":
            B[int(loc[1])] = symbol
            return True
        
    elif loc[0] == "C":
        if C[int(loc[1])] == " ":
            C[int(loc[1])] = symbol
            return True

def tictactoe():
    global A, B, C

    #by row
    if all(x == A[0] != " " for x in A):
            return True
    elif all(y == B[0] != " " for y in B):
            return True
    elif all(z == C[0] != " " for z in C):
            return True
        
    #by diagonal
    elif A[0] == B[1] == C[2] != " ":
            return True
    elif A[2] == B[1] == C[0] != " ":
        return True
    
    #by column
    for i in range(3):
        if A[i] == B[i] == C[i] != " ":
            return True 

def series():
    if turn == 9:
        print("Series!")
        return True

#create board land
A = [" ", " ", " "]
B = [" ", " ", " "]
C = [" ", " ", " "]

logo = """
  _______        ______             ______         
 /_  __(_)____  /_  __/___ ______  /_  __/___  _____
  / / / / ___/   / / / __ `/ ___/   / / / __ \/ _  /
 / / / / /__    / / / /_/ / /__    / / / /_/ /  __/
/_/ /_/\___/   /_/  \__,_/\___/   /_/  \____/\___/ \n"""
print(logo)
enemy = "X"

#player role choose  
roles = ["X", "O"]
player = input("Choose your symbol (X/O): ").upper()
show_board(starting_game=True)

turn = 0
while turn < 9:
    #X role will get first turn
    filled = True
    if player == "X":
        enemy = "O"

        print("\nYour turn,")
        while filled:
            loc = input("Mark the field: ").upper()

            if check_and_mark(loc, symbol=player):
                show_board()
                filled = False
            else:
                 print("\nThe field has been filled in!\n")
        if tictactoe():
            print("You win!")
            break

        turn += 1
        if series():
           break

    #enemy auto mark
    print("\nEnemy turn,")
    time.sleep(2)
    looping = True
    while looping:
        rand_loc = random.choice(["A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2"])
        if check_and_mark(rand_loc, symbol=enemy):
            show_board()
            looping = False
    if tictactoe():
        print("You lose!")
        break
    turn += 1
    if series():
           break

    # if player choose O
    filled = True
    if player == "O":
        enemy = "X"
        print("\nYour turn,")
        while filled:
            loc = input("Mark the field: ").upper()

            if check_and_mark(loc, symbol=player):
                show_board()
                filled = False
            else:
                 print("\nThe field has been filled in!\n")
        if tictactoe():
            print("You win!")
            break
        turn += 1
        if series():
           break

