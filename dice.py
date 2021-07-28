import time
import random


def dice():
    player_draw = random.randint(1, 6)
    print("You rolled " + str(player_draw))

    ai_draw = random.randint(1, 6)
    print("The computer rolls...")
    time.sleep(2)
    print()
    print("Computer rolled " + str(ai_draw))

    if player_draw > ai_draw:
        print("You win!")
    elif player_draw == ai_draw:
        print("Tie game.")
    else:
        print("You lose.")

    print()
    print("Quit? (yes/no)")
    shell_we_quit = input().lower()
    if shell_we_quit == "yes":
        exit()
    elif shell_we_quit == "no":
        pass
    else:
        print("I didn't understand that. Playing again.")


while True:
    print("Please press ENTER to roll your die.")
    roll = input()
    dice()
