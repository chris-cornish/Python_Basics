import random

def game():
    guesses = []

    try:
        # generate a user-defined number between 1 and 10
        user_num = int(input("Pick a number between 1 and 10: "))
    except ValueError:
        print("{} isn't a number!".format(user_num))

    #have computer guess
    computer_guess = random.randint(1, 10)

    while True:
        if computer_guess == user_num:
            guesses.append(computer_guess)
            print("The computer has guessed your secret number of {} in {} tries.".format(user_num, len(guesses)))
            break
        elif computer_guess < user_num:
            guesses.append(computer_guess)
            print("The number is higher than {}".format(computer_guess))
            computer_guess = random.randint(computer_guess + 1, 10)
        else:
            guesses.append(computer_guess)
            print("The number is lower than {}".format(computer_guess))
            computer_guess = random.randint(1, computer_guess - 1)
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")
game()
