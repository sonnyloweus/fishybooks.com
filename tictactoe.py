sep1 = "---+---+---"

num = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

divider = ["|","|","\t"]

num_str = [[" 1 "," 2 "," 3 "],
           [" 4 "," 5 "," 6 "],
           [" 7 "," 8 "," 9 "]]

xo_str = ["   "," x "," o "]

counter = 1

stopper = 0

########################################################################################################################

def print_board():
    for n in range(3):
        for a in range(3):
            print(xo_str[num[n][a]],end=divider[a])
        
        for i in range(3):
            if num[n][i]==0:
                print(num_str[n][i],end=divider[i])
            else:
                print("   ",end=divider[i])
        print()
        
        if n!=2:
            print(sep1 + "\t" + sep1)

########################################################################################################################

def check_game_over():
    for i in range(3):
        if xo_str[num[i][0]]== xo_str[num[i][1]] and xo_str[num[i][1]]== xo_str[num[i][2]] and xo_str[num[i][0]]!= "   ":
            print_board()
            print("Team",xo_str[num[i][1]],"has won")
            return 1
    for i in range(3):
        if xo_str[num[0][i]]== xo_str[num[1][i]] and xo_str[num[1][i]]== xo_str[num[2][i]] and xo_str[num[0][i]]!= "   ":
            print_board()
            print("Team",xo_str[num[0][i]],"has won")
            return 1
    if xo_str[num[0][0]]== xo_str[num[1][1]] and xo_str[num[2][2]]== xo_str[num[1][1]] and xo_str[num[2][2]]!= "   ":
        print_board()
        print("Team",xo_str[num[0][0]],"has won")
        return 1
    if xo_str[num[0][2]]== xo_str[num[1][1]] and xo_str[num[2][0]]== xo_str[num[1][1]] and xo_str[num[2][0]]!= "   ":
        print_board()
        print("Team",xo_str[num[1][1]],"has won")
        return 1
    return 0

########################################################################################################################

def check_space_ai():
    for i in range(3):
        if xo_str[num[i][0]]== xo_str[num[i][1]] and xo_str[num[i][1]]== xo_str[num[i][2]] and xo_str[num[i][0]]!= "   ":
            return 1
    for i in range(3):
        if xo_str[num[0][i]]== xo_str[num[1][i]] and xo_str[num[1][i]]== xo_str[num[2][i]] and xo_str[num[0][i]]!= "   ":
            return 1
    if xo_str[num[0][0]]== xo_str[num[1][1]] and xo_str[num[2][2]]== xo_str[num[1][1]] and xo_str[num[2][2]]!= "   ":
        return 1
    if xo_str[num[0][2]]== xo_str[num[1][1]] and xo_str[num[2][0]]== xo_str[num[1][1]] and xo_str[num[2][0]]!= "   ":
        return 1
    return 0

########################################################################################################################

def is_board_full():
    for n in range(3):
        for i in range(3):
            if xo_str[num[n][i]] == "   ":
                return False

    return True

########################################################################################################################

def mark():
    turn = int(input("Write the number corresponding to the spot you want to mark:"))
    turn -= 1
    
    col = turn%3
    row = turn//3

    if num[row][col]== 1 or num[row][col]==2:
        print("Spot Already Taken. Pick a new spot.")
        mark()
    else:
        num[row][col] = 1

########################################################################################################################

def ai_mark():
    
    empty = 0
    for n in range(3):
        for i in range(3):
            if num[i][n] == 0:
                empty +=1
    
    aiRandom = 0
    
    for n in range(3):
        for i in range(3):
            if num[i][n] == 0:
                num[i][n] = 2
                ai_stopper = check_space_ai()
                if ai_stopper == 1:
                    num[i][n] = 2
                    aiRandom = 3
                    break
                else:
                    num[i][n] = 0
                    aiRandom = 1
        if aiRandom == 3:
                break

    if aiRandom == 1:          
        for n in range(3):
            for i in range(3):
                if num[i][n] == 0:
                    num[i][n] = 1
                    ai_stopper = check_space_ai()
                    if ai_stopper == 1:
                        num[i][n] = 2
                        aiRandom = 3
                        break
                    else:
                        num[i][n] = 0
                        aiRandom = 1
            if aiRandom == 3:
                    break

    if empty == 8:
        if num[1][1] == 0:
            num[1][1] = 2
            aiRandom = 3
        elif num[1][1] == 1:
            num[0][0] = 2
            aiRandom = 3
            
    if empty == 6:
        if num[1][2] == 1 and num[2][1] == 1:
            num[2][2] = 2
            aiRandom = 3
        elif num[0][1] == 1 and num[1][2] == 1:
            num[0][2] = 2
            aiRandom = 3
        elif num[1][0] == 1 and num[2][1] == 1:
            num[2][0] = 2
            aiRandom = 3
        ##
        elif num[0][2] == 1 and num[2][0] == 1:
            num[1][2] = 2
            aiRandom = 3
        ##           
        elif num[1][2] == 1 and num[0][0] == 1:
            num[2][2] = 2
            aiRandom = 3
        elif num[1][2] == 1 and num[2][0] == 1:
            num[0][2] = 2
            aiRandom = 3
        elif num[0][0] == 1 and num[2][1] == 1:
            num[2][2] = 2
            aiRandom = 3
        elif num[0][2] == 1 and num[2][1] == 1:
            num[2][0] = 2
            aiRandom = 3
        ##
        elif num[1][1] == 1 and num[2][2] == 1:
            num[2][0] = 2
            aiRandom = 3
                    
    if aiRandom == 1:
        for n in range(3):
            for i in range(3):
                if num[i][n] == 0:
                    num[i][n] = 2
                    aiRandom = 2
                    break
            if aiRandom == 2:
                break

    aiRandom = 0

########################################################################################################################


play = 0
ai_wins = 0
player_wins = 0

print_board()

while stopper != 1:

    if play%2 == 0:
        mark()
        
        stopper = check_game_over()
        if stopper == 1:
            player_wins+=1
        if stopper != 1 and is_board_full()== True:
            stopper = 1
            print_board()
            print("Tie Game! Everybody wins.")           
    else:    
        ai_mark()
        stopper = check_game_over()
        if stopper == 1:
            ai_wins+=1
        if stopper != 1 and is_board_full()== True:
            stopper = 1
            print_board()
            print("Tie Game! Everybody wins.")
        if stopper != 1:
            print_board()
            print("Computer has made its move. Your turn.")

    if stopper == 1:
        print("Score is: computer =",ai_wins," player =",player_wins)
        restart = input("Would you like to try again? yes/no : ")
        if restart == "yes":
            stopper = 0
            num = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
            print_board()
            play = -1
        else:
            stopper = 1
            print("Ok. Final Score is: computer =",ai_wins," player =",player_wins)
            if ai_wins > player_wins:
                print("Final Standings: Computer wins!")
            elif ai_wins == player_wins:
                print("Final Standings: Tie! Everybody wins!")

    play+=1









    
