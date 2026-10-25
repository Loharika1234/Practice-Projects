import random #import random module

moves=["rock", "paper", "scissor" ]#list created for moves
#function to make computer to chosse a random move from moves[]
def get_comp():
    return random.choice(moves)
#funxtion to check who won the game
def check_who_win(p,c):
    if p>c:
        print("You Win..🎉🎉")
    elif c>p:
        print("Computer Wins..🎉🎉😁")
    else:
        print(" draw🤝" )    
#game logic
def get_winner(i):
    comp=0
    play=0
    while(i>0):
        player=input("choose rock,paper or scissor:").lower()
        if player not in moves:
            print("invalid input")
        else:
            computer=get_comp()
            print("you choose:", player )
            print("computer chose:" ,computer)
            winning_moves={
                 "rock" :"scissor",
                 "scissor":"paper",
                 "paper":"rock"
            }  
    
            if winning_moves[player]==computer:
                 play+=1
            elif computer==player:
                 print("draw")
            else:
                comp+=1   
            print("player score:" ,play)
            print("comp score: " ,comp) 
        i-=1 
        if i==0:
            break  
    check_who_win(play,comp)

            
n=int(input("how many games you want to play:"))  #input how many games you want to play
get_winner(n)
