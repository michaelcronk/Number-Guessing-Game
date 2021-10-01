import random

# You can insert the desired range of numbers you'd like to use below
random_num = random.randint(1, 10)
# You can update how many attempts you'd like to have
attempts = 3


def exit_game():
    print("Thank you for playing! Until next time...")
    exit()


while attempts != 0:
    try:
        guess = input("Guess a number between 1 and 10: ")
        if str(guess).lower() in ["exit"]:
            exit_game()
        guess = int(guess)
        attempts -= 1
        if guess == random_num:
            print("You've guessed the right number!\n")
            ask_try_again = input("Would you like to play again? Y or N:  ")
            if ask_try_again.lower() in ['yes', 'y']:
                continue
            elif ask_try_again.lower() in ["no", "n"]:
                exit_game()
            else:
                exit()
        elif guess != random_num:
            if attempts != 0:
                print("Wrong guess, try again! {} attempts remaining".format(attempts))
                continue
            else:
                ask_try_again = input(
                    "You've ran out of tries... Wanna try again? Y or N:  ")
                if ask_try_again.lower() in ['yes', 'y']:
                    attempts = 3
                    continue
                elif ask_try_again.lower() in ["no", "n"]:
                    exit_game()
                else:
                    raise ValueError
        else:
            exit()
    except ValueError:
        print("Invalid entry, try again...\n")
        continue
