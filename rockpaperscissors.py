import random
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
       return "It's a Tie!"
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            return "Computer Wins!"
        else:
            return "You Win!"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "Computer Wins!"
        else:
            return "You Wins!"
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            return "Computer Wins!"
        else:
            return "You Win!"
    else:
        return "Invalid input.Please choose another choice"
def play_game():
    user_choice=input("rock,paper,scissors")
    computer_choice=random.choice("rock,paper,scissors")
    print("You choose:",user_choice)
    print("Computer choose:",computer_choice)
    print(determine_winner(user_choice,computer_choice))
play_game()
    
        
