### Final Project - Tic Tac Toe by Andrya Pimentel ###

import random
import time

# Function for introductions
def intro():
    time.sleep(4)
    global spot
    spot = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    global user_name
    user_name = input("\nHello! My name is Ty! What is your name? ")
    print(f"\nHello, {user_name}!\n")
    time.sleep(2)
    print("Are you ready to play...")
    time.sleep(2)
    print ("""
     |     |
  T  |  I  |  C
_____|_____|_____
     |     |
  T  |  A  |  C
_____|_____|_____
     |     |
  T  |  O  |  E
     |     |       ? """)


# Function to ask user if they want to play
def want_play():
    answer = input("\nEnter Yes or No: ")
    if answer == "Yes":
        print("\nGreat! Let's begin!")
    elif answer == "No":
        print("\nWell, too bad! We are playing anyway. Let's begin!")
    else:
        print("\nOops! Invalid syntax. Please try again.")
        want_play()


# Function for user to choose X or O for game
def choose():
    time.sleep(1)
    global user_symbol
    user_symbol = input("\nChoose your weapon! Input X or O: ")
    global comp_symbol
    if user_symbol == "X":
        print(f"\nGreat choice, {user_name}!")
        comp_symbol = "O"
    elif user_symbol == "O":
        print(f"\nGreat choice, {user_name}!")
        comp_symbol = "X"
    else:
        print("\nOops! Invalid syntax. Please try again.")
        choose()
        
        
# Function to print game board
def print_game():
    print(f"""
     |     |
  {spot[0]}  |  {spot[1]}  |  {spot[2]}
_____|_____|_____
     |     |
  {spot[3]}  |  {spot[4]}  |  {spot[5]}
_____|_____|_____
     |     |
  {spot[6]}  |  {spot[7]}  |  {spot[8]}
     |     |       """)
     

# Function for user's turn
def user_turn():
    if all(isinstance(x, str) for x in spot) == False:
        time.sleep(1)
        position = input("\nYour turn! Choose a position by inputting the number: ")
        if str.isnumeric(position) == False:
            print("\nOops! Invalid syntax. Please try again.")
            user_turn()
        else:
            index = int(position) - 1
            if index > 8 or index < 0: 
                print("\nOops! That spot does not exist. Please choose what is available.")
                user_turn()
            elif isinstance(spot[index],int) == True:
                    spot[index] = user_symbol
            else:
                print("\nOops! That spot is taken. Please choose another.")
                user_turn()
        
    
# Function for computer's turn
def computer_turn():
    if all(isinstance(x, str) for x in spot) == False:
        print("\nMy turn!")
        int_array = []
        for m in range(0,9):
            if isinstance(spot[m],int) == True:
                int_array.append(spot[m])
        i = random.randint(0,len(int_array)-1)
        j = int_array[i]-1
        spot[j] = comp_symbol
        
      
# Function to check if someone won      
def check():
    if (spot[0]==spot[1]==spot[2]==comp_symbol) or \
    (spot[3]==spot[4]==spot[5]==comp_symbol) or \
    (spot[6]==spot[7]==spot[8]==comp_symbol) or \
    (spot[0]==spot[3]==spot[6]==comp_symbol) or \
    (spot[1]==spot[4]==spot[7]==comp_symbol) or \
    (spot[2]==spot[5]==spot[8]==comp_symbol) or \
    (spot[0]==spot[4]==spot[8]==comp_symbol) or \
    (spot[2]==spot[4]==spot[6]==comp_symbol):
        return "1"
    elif (spot[0]==spot[1]==spot[2]==user_symbol) or \
    (spot[3]==spot[4]==spot[5]==user_symbol) or \
    (spot[6]==spot[7]==spot[8]==user_symbol) or \
    (spot[0]==spot[3]==spot[6]==user_symbol) or \
    (spot[1]==spot[4]==spot[7]==user_symbol) or \
    (spot[2]==spot[5]==spot[8]==user_symbol) or \
    (spot[0]==spot[4]==spot[8]==user_symbol) or \
    (spot[2]==spot[4]==spot[6]==user_symbol):
        return "2" 
    elif all(isinstance(x, str) for x in spot) == True:
        return "3"
   
   
# Function to emphasize three-in-a-row
def final_board():
    if (spot[0]==spot[1]==spot[2]):
        spot[3] = " "
        spot[4] = " "
        spot[5] = " "
        spot[6] = " "
        spot[7] = " "
        spot[8] = " "
    elif (spot[3]==spot[4]==spot[5]):
        spot[0] = " "
        spot[1] = " "
        spot[2] = " "
        spot[6] = " "
        spot[7] = " "
        spot[8] = " "
    elif (spot[6]==spot[7]==spot[8]):
        spot[0] = " "
        spot[1] = " "
        spot[2] = " "
        spot[3] = " "
        spot[4] = " "
        spot[5] = " " 
    elif (spot[0]==spot[3]==spot[6]):
        spot[1] = " "
        spot[2] = " "
        spot[4] = " "
        spot[5] = " "
        spot[7] = " "
        spot[8] = " "  
    elif (spot[1]==spot[4]==spot[7]):
        spot[0] = " "
        spot[2] = " "
        spot[3] = " "
        spot[5] = " "
        spot[6] = " "
        spot[8] = " "
    elif (spot[2]==spot[5]==spot[8]):
        spot[0] = " "
        spot[1] = " "
        spot[3] = " "
        spot[4] = " "
        spot[6] = " "
        spot[7] = " "
    elif (spot[0]==spot[4]==spot[8]):
        spot[1] = " "
        spot[2] = " "
        spot[3] = " "
        spot[5] = " "
        spot[6] = " "
        spot[7] = " "
    elif (spot[2]==spot[4]==spot[6]):
        spot[0] = " "
        spot[1] = " "
        spot[3] = " "
        spot[5] = " "
        spot[7] = " "
        spot[8] = " "


# Function to show who won     
def who_won():
    case = check()
    if case == "1":
        final_board()
        time.sleep(1.5)
        print_game()
        print(f"\nI win! Better luck next time, {user_name}.")
        return "end"
    elif case == "2":
        final_board()
        time.sleep(1.5)
        print_game()
        print(f"\nCongratulations, {user_name}! You win! Great game!")
        return "end"
    elif case == "3":
        final_board()
        time.sleep(1.5)
        print_game()
        print(f"\nIt's a tie! No one wins.")
        return "end"


# Function for game to execute
def lets_play():
    done = False
    time.sleep(1)
    first = input("\nWould you like to go first? Enter Yes or No: ")
    if first == "Yes":
        print("\nGo for it!")
        time.sleep(2)
        print("\nHere is the game board:")
        print_game()
        while done == False:
            user_turn()
            time.sleep(1)
            if who_won() == "end":
                break
            print_game()
            time.sleep(1)
            computer_turn()
            time.sleep(2.5)
            if who_won() == "end":
                break
            print_game()
        play_again()  
    elif first == "No":
        print("\nWhy thank you!")
        time.sleep(2)
        print("\nHere is the game board:")
        print_game()
        while done == False:
            time.sleep(1)
            computer_turn()
            time.sleep(2.5)
            if who_won() == "end":
                break
            print_game()
            user_turn()
            time.sleep(1)
            if who_won() == "end":
                break
            print_game()
        play_again()  
    else:
        print("\nOops! Invalid syntax. Please try again.")
        lets_play()
        
        
# Function to ask user to play again
def play_again():
    time.sleep(1)
    again = input("\nDo you want to play again? Enter Yes or No: ")
    if again == "Yes":
        choose()
        global spot 
        spot = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #print_game()
        lets_play()
    elif again == "No":
        time.sleep(1)
        input("\nFine! Leave then. Press ENTER to exit.")  
    else:
        print("\nOops! Invalid syntax. Please try again.")
        play_again()
    

# Section to begin game
intro()
want_play()
choose()
lets_play()


        
        
   