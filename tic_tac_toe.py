import os

# python3.8.10
# a cli tic-tac-toe app

# functions 
def display_title_bar(menu_mode):
    # general purpose "menu_mode" variable to show menu
    print("\n-----------------------------------")
    print(f"--- tic tac toe --- [{menu_mode}]\t---")
    print("-----------------------------------")
        
def clear():
    os.system("clear")

def get_choice():
    # display menu
    print("")
    print("menu:")
    print("1 - play")
    print("Q - quit")

    # get user input
    choice = input("\ninput[1, Q]:\n> ")
    return choice

def display_error_message():
    print("I didn't quite get what you meant. Can you repeat that?")

def display_board(menu_mode, player, turn, invalid_input):
    clear()
    display_title_bar(menu_mode)

    # display warning for wrong inputs
    if invalid_input:
        display_error_message()
        invalid_input = False

    # display whose turn to play (X or O) and current turn number:
    # X's turn - turn n:
    print(f"{player}'s turn - turn {turn}:\n")

    # display tic-tac-toe playing board
    for index, row in enumerate(numbers):
        for index2, column in enumerate(row): 
            try:
                number = int(column)
                if number%3 != 0:
                    print(f"{number} | ", end="")
                else:
                    print(number)
            except:
                if numbers2[index][index2] %3 != 0:
                    print(f"{column} | ", end="")
                else:
                    print(column)

        # separate rows
        if index < 2:
            print("---------")    

def fill_board(choice, player):
    # fill board with player mark (X or O)
    for index, row in enumerate(numbers):
        for index2, column in enumerate(row):
            if column == choice:
                numbers[index][index2] = player

def get_player_choice():
    # get and return user input
    choice = input("\nchoose[1-9, Q]:\n> ")
    return choice

def quit_message():
    print("Thanks for playing! bye-bye!")

def tic_tac_toe():
    # initialize variables
    invalid_input = False
    match_finished = False
    choice = ""
    turn = 1

    # clear the terminal and display header
    clear()
    display_title_bar("human")
    
    # keep playing until winner is found or user quits (Q)
    while choice != "Q":
        # adjust turn counter to not overflow
        if match_finished:
            turn -= 1

        # determine X or O turn to play
        if turn%2 == 0:
            player = "O"
        else:
            player = "X"

        # display playing board
        display_board("human", player, turn, invalid_input)

        # get user choice: 1-9 or Q(uit) until game is finished
        if match_finished is False:
            choice = get_player_choice()
        elif match_finished and winner:
            # if game is finished, game displays the winner or a draw
            print(f"\nPlayer {winner} wins!")
            quit_message()
            return "Q"
        else:
            print("\nIt's a Draw!")
            quit_message()
            return "Q"

        # checks for invalid input (anything else that's not 1-9 or "Q")
        if choice not in valid_inputs:
            invalid_input = True

            # don't increment turn counter for invalid inputs via "continue"
            continue
        else:
            # if valid, remove choice in valid inputs
            #  because it's already been selected
            valid_inputs.remove(choice)
            invalid_input = False

        # mark board with X or O with valid input
        fill_board(choice, player)

        # flatten "numbers" array to check winner
        flat_numbers = flatten_2d_array(numbers)

        # check for winners
        winner = check_winner(player, flat_numbers)
        remaining_valid_inputs = len(valid_inputs)
        if winner or remaining_valid_inputs == 0:
            match_finished = True

        # increment turn counter for valid inputs
        turn += 1

def flatten_2d_array(numbers):
    flat_array = []
    for index, row in enumerate(numbers):
        for index2, column in enumerate(row):
            flat_array.append(numbers[index][index2])

    return flat_array

def check_winner(player, numbers):
    # initialize arrays
    row1 = []
    row2 = []
    row3 = []

    column1 = []
    column2 = []
    column3 = []

    backslash = []
    forward_slash = []

    # fill arrays with user input
    for index, number in enumerate(numbers):
        # fill rows
        if index <= 2:
            row1.append(number)
        elif index <= 5:
            row2.append(number)
        else:
            row3.append(number)

        # fill columns
        if index in column1_indices:
            column1.append(number)
        elif index in column2_indices:
            column2.append(number)
        else:
            column3.append(number)
    
        # fill diagonals
        if index in backslash_indices:
            backslash.append(number)
        if index in forward_slash_indices:
            forward_slash.append(number)
    
    # find winner
    winner = ""
    marks = []
    winner_found = False

    # count player "marks" in every possible line
    for index, player in enumerate(players):
        # check rows
        marks.append(row1.count(player))
        marks.append(row2.count(player))
        marks.append(row3.count(player))
        
        # check columns
        marks.append(column1.count(player))
        marks.append(column2.count(player))
        marks.append(column3.count(player))
        
        # check diagonals
        marks.append(backslash.count(player))
        marks.append(forward_slash.count(player))

        # check if "player" has gotten 3 marks in a line
        for mark in marks:
            if mark == 3:
                winner = player
                winner_found = True

        # return player winner (X or O) if found
        #  else, it returns False
        if winner_found:
            return winner
        elif winner_found is False and player == "O":
            return False
        
        # clear mark count for each player check
        marks = []

# end of functions
# prepare variables for main program
numbers = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]

numbers2 = [[1,2,3],
            [4,5,6],
            [7,8,9]]

valid_inputs = ["1", "2", "3",
                "4", "5", "6",
                "7", "8", "9",]

column1_indices = [0, 3, 6]
column2_indices = [1, 4, 7]

backslash_indices = [0, 4, 8]
forward_slash_indices = [2, 4, 6]

players = ["X", "O"]

choice = ""
invalid_input = False

# main program
while choice != "Q":
    clear()
    display_title_bar("main menu")

    # reset playing board
    numbers_copy = [["1", "2", "3"],
                    ["4", "5", "6"],
                    ["7", "8", "9"]]

    valid_inputs_copy = ["1", "2", "3",
                         "4", "5", "6",
                         "7", "8", "9",]

    # restore default values
    numbers = numbers_copy
    valid_inputs = valid_inputs_copy

    # warn for invalid input
    if invalid_input:
        display_error_message()
    
    # get user choice
    choice = get_choice()

    # respond to user choice
    if choice == "1":
        choice = tic_tac_toe()
    elif choice == "Q":
        quit_message()
    else:
        invalid_input = True
