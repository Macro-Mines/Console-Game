# PYTHON PROJECT  | PLAY GAMES
# !           --- README ---
#   This sign --> # | is a comment
# ? This sign --> ? | change the comments to blue
# * This sign --> * | change the comments to green
# ! This sign --> ! | change the comments to red


#  DocString is written under  # ! DocString :
#  Codes are written under # * : CODE -->
#  Write te instructions about the code under # * : INSTRUCTIONS -->
#  User or Player mentioned in the code is one who is playing this game

# !  ------ LIBRARY IMPORT -------

import random

# random library is used to generate random choice from given parameters

from time import sleep

# sleep delays the code execution time

import datetime

# datetime library will give us the current time and date

import string

# string library will generate ascii letters

import pandas as pd

# Pandas library is used read files

import numpy as np

import matplotlib.pyplot as plt

# * ASCII ARTS -->

rock_art = """
                              $$\       
                              $$ |      
 $$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\ 
$$  __$$\ $$  __$$\ $$  _____|$$ | $$ /
$$ |  \__|$$ /  $$ |$$ /      $$$$$$$/ 
$$ |      $$ |  $$ |$$ |      $$  _$$\  
$$ |      \$$$$$$  |\$$$$$$$\ $$ | \$$\ 
\__|       \______/  \_______|\__|  \__|
"""


paper_art = """
  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
 /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$ /$$__  $$| $$  | $$| $$_____/| $$      
| $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
| $$____/  \_______/| $$____/  \_______/|__/      
| $$                | $$                          
| $$                | $$                          
|__/                |__/                          
"""


scissor_art = """
                    $$\                                         
                    \__|                                        
 $$$$$$$\  $$$$$$$\ $$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\  
$$  _____|$$  _____|$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ 
\$$$$$$\  $$ /      $$ |\$$$$$$\  \$$$$$$\  $$ /  $$ |$$ |  \_/
 \____$$\ $$ |      $$ | \____$$\  \____$$\ $$ |  $$ |$$ |      
$$$$$$$  |\$$$$$$$\ $$ |$$$$$$$  |$$$$$$$  |\$$$$$$  |$$ |      
\_______/  \_______|\__|\_______/ \_______/  \______/ \__|      
"""


rock = """  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
"""

paper = """  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
"""

scissors = """  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
"""


pg = """

  ___   _        _    __   __               ___     _     __  __   ___   ___    
 | _ \ | |      /_\   \ \ / /     ___      / __|   /_\   |  \/  | | __| / __|   
 |  _/ | |__   / _ \   \ V /     |___|    | (_ |  / _ \  | |\/| | | _|  \__ \   
 |_|   |____| /_/ \_\   |_|                \___| /_/ \_\ |_|  |_| |___| |___/   
                                                                                

"""


# !------------------------------ R-P-S |  G A M E    C O D E S  --------------------------------- #


def computer_choice():
    # * : INSTRUCTIONS -->

    """computer_choice function() :

    Returns:
        int: return randomly any one of the number | 1 - 2 - 3 |
    """
    # ? computer will choose its number : 1 or 2 or 3
    # * : CODE -->

    number = random.randint(1, 3)
    return number


def user_choice():

    # * : INSTRUCTIONS -->

    # ! DocString:
    """user_choice functon() : user have to choose a number
                               from | 1 - 2 - 3 |
    Returns:
        int : number user has input
    """
    # user will choose its number 1:Rock , 2:Paper, 3:Scissor
    # * : CODE -->

    number = ""
    while number not in ["1", "2", "3"]:
        number = input("\n\n>> Enter 1:Rock,  2:Paper,  3:Scissor - ").strip()
    return int(number)


def check(num1, num2):
    # * : INSTRUCTIONS -->

    # ! DocString :
    """check functin() : check conditions b/w num1 and num2

    Args:
        num1 (int): number choosen by the computer
        num2 (int): number choosen by the user
    """
    # it will check the condition and return the game result
    # *     1 : rock
    # *     2 : paper
    # *     3 : scissors

    # ! HOW TO SELECT THE WINNER :
    # ?     YOU WIN IF :
    # *        COMPUTER CHOOSE | USER CHOOSE
    # *               (num1)   |   (num2)
    # *                  1     |     2
    # *                  2     |     3
    # *                  3     |     1

    # * : CODE -->
    # * return 1 : Player won
    # * return 2 : Its a Tie
    # * return 3 : Computer Won

    if (
        (num1 == 1 and num2 == 2)
        or (num1 == 2 and num2 == 3)
        or (num1 == 3 and num2 == 1)
    ):
        return 1
    elif num1 == num2:
        return 2
    else:
        return 3


def play_game():
    # ! DocString:
    """play_game function()
    allows the player to play
    the game 1 single time
    """
    # * : STEPS -->
    # ?      num1 = will store integer return by computer_choice()
    # ?      num2 = will store integer return by user_choice()
    # *      check(num1, num2) : jump to check() function to see what it does

    # * : CODE -->

    lst = {"1": rock, "2": paper, "3": scissors}
    num1 = computer_choice()
    num2 = user_choice()

    time = datetime.datetime.now()
    print(f"--------------------\n >> You choose: {lst[str(num2)]}")
    print(f"\n >> Computer choose: {lst[str(num1)]}")
    sleep(0.5)
    winner = check(num1, num2)
    if winner == 1:
        print(" -->  YOU  WON  <--")
    elif winner == 2:
        print(" -->  ITS  A  TIE  <--")
    elif winner == 3:
        print(" -->  YOU  LOOSE  <--")
    print("______________________")

    dic = {"1": "ROCK", "2": "PAPER", "3": "SCISSORS"}
    win_dic = {"1": "You Won", "2": "Its a Tie", "3": "You Loose"}
    with open("GameRecords.csv", "a") as gameRecords:
        gameRecords.write(
            f"\n{time},{dic[str(num1)]},{dic[str(num2)]},{win_dic[str(winner)]},{winner}"
        )


def play_again():
    # ! DocString -->
    """play_again() : this function asks the user
    if he wants to play again or not (game 1)
    """
    # ? it will ask the player to play again after each match
    # * : CODE -->

    sleep(1.5)
    print("\n------------------------------------------------------------------")
    play_input = ""
    while play_input not in ["n", "y", "yes", "no", "x", "X"]:
        play_input = (
            input(
                "\n\n>> Enter Y to play again | or  N to quit | or X to change the game :  "
            )
            .strip()
            .lower()
        )

    if play_input in ["y", "yes"]:
        play_game()
        play_again()

    if play_input == "x":
        print("\n\n THE WIN-LOOSE RATIO OF THE ROCK/PAPER/SCISORS GAME : ")
        show_graph()
        sleep(4)
        play_the_games()


def show_graph():
    scores = pd.read_csv("GameRecords.csv")

    a = scores[scores["WINNER_NO"] == 1].shape[0]
    b = scores[scores["WINNER_NO"] == 2].shape[0]
    c = scores[scores["WINNER_NO"] == 3].shape[0]

    x = np.array(["WON", "TIE", "LOOSE"])
    y = np.array([a, b, c])

    plt.bar(x, y)
    plt.show()


def rating_the_game():
    # ! DocString -->
    """rating_the_game() : ask the player
    what rating he
    wants to give ?
    """

    # * : CODE -->

    print(
        "\n-------------------------------------\n ||  WELCOME TO GAME RATING PORTAL  ||\n--------------------------------------"
    )
    print(
        """
        5 star : * * * * *
        4 star : * * * *
        3 star : * * *
        2 star : * *
        1 star : *
        """
    )
    print("--------------------------------------")

    rating_dict = {"1": "*", "2": "* *", "3": "* * *", "4": "* * * *", "5": "* * * * *"}

    rate = ""
    while rate not in ["1", "2", "3", "4", "5"]:
        rate = input(
            "\n >> What rating you would like to give from 1 to 5 ? :  "
        ).strip()
        if rate not in ["1", "2", "3", "4", "5"]:
            print("        [x] -- Enter valid rating digit")

    print(f"\n\n   :) Thank you for giving rating of {rate} : {rating_dict[rate]}")
    print("------------------------------------------------------------------")
    exit_the_game()


def rate_it():
    """rate_it()
    it will ask the player
    if he wants to rate the
    game or not
    """
    # * : CODE -->

    rate_input = (
        input("\n >> Would you like to rate the game | yes or no | ? :  ")
        .strip()
        .lower()
    )

    if rate_input in ["y", "yes"]:
        rating_the_game()
    elif rate_input in ["n", "no"]:
        print(
            "\n-----------------------------------------------------------------------"
        )
        print("           [-][-][-]   Thank you for playing this game   [-][-][-]")
        print("-----------------------------------------------------------------------")
        exit_the_game()
    else:
        rate_it()


def play_the_game_1():
    """play_the_game_1 function():
    this function executes all
    game functions in order to
    play the game.
    """
    # ? Asking the user to input whether he knows to play the game or not

    # * : CODE -->
    sleep(1)
    print(rock_art)

    sleep(1.5)
    print(paper_art)

    sleep(1.5)
    print(scissor_art)

    while True:
        know = (
            input("\n\n >>  Do you know how to play this game YES | NO  ? :  ")
            .strip()
            .lower()
        )

        if know in ["y", "yes"]:
            play_game()
            play_again()
            rate_it()
            break

        elif know in ["n", "no"]:
            print(
                "\n >> Visit this link to learn this game --> : https://wrpsa.com/the-official-rules-of-rock-paper-scissors/"
            )
            exit_the_game()
        else:
            pass


#!-------------------------------- E N D    O F  R-P-S  G A M E    C O D E S -----------------------------#

#!--------- Guess Game---------
gg = """

   ___   _   _   ___   ___   ___   ___   _  _    ___            ___     _     __  __   ___    _   
  / __| | | | | | __| / __| / __| |_ _| | \| |  / __|   ___    / __|   /_\   |  \/  | | __|  (_)  
 | (_ | | |_| | | _|  \__ \ \__ \  | |  | .` | | (_ |  |___|  | (_ |  / _ \  | |\/| | | _|    _   
  \___|  \___/  |___| |___/ |___/ |___| |_|\_|  \___|          \___| /_/ \_\ |_|  |_| |___|  (_)  
                                                                                                  

"""


def play_the_game_2():
    number = random.randint(1, 10)

    number_of_guesses = 0
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(
        "\n>> Okay! Computer is guessing a number between 1 and 10 [endpoints included]: "
    )
    sleep(3)
    print(">> You have to guess the right number within 3 chance")
    print(".\n.\n.")
    sleep(4)
    print(">> Now guess the number . . . ")
    while number_of_guesses < 3:
        guess = input("\n>> Guess the number : ").strip()
        while not guess.isdigit():
            print("   [x] Enter integer from 1 to 10")
            guess = input("\n>> Guess the number : ").strip()
        number_of_guesses += 1
        if int(guess) < number:
            print("  [>] -- Your guess is too low")
        if int(guess) > number:
            print("  [<] -- Your guess is too high")
        if int(guess) == number:
            print("  [*] -- Correct Guess")
            break
    if int(guess) == number:
        print("\n>> You guessed the number in " + str(number_of_guesses) + " tries!")
    else:
        print("\n>> You did not guess the number, The number was " + str(number))

    play_again_2()


def play_again_2():
    # ! DocString -->
    """play_again_2() : this function asks the user
    if he wants to play again or not
    """
    # ? it will ask the player to play again after each match
    # * : CODE -->

    print("\n------------------------------------------------------------------")
    play_input = (
        input(">> Enter Y to play again | or  N to quit | or X to change the game :  ")
        .strip()
        .lower()
    )
    print("------------------------------------------------------------------")
    while play_input not in ["n", "y", "yes", "no", "x", "X"]:
        play_input = (
            input(
                ">> Enter Y to play again  | or  N to quit | or X to change the game :  "
            )
            .strip()
            .lower()
        )
        print("------------------------------------------------------------------")

    if play_input in ["y", "yes"]:
        play_the_game_2()
    elif play_input in ["x"]:
        play_the_games()
    else:
        rate_it()


# ! Dice Game -->

# Rolling the dice game : lets check who will get the first six
dd = """

 ____  ____  ___  ____       ___    __    __  __  ____ 
(  _ \(_  _)/ __)( ___)     / __)  /__\  (  \/  )( ___)
 )(_) )_)(_( (__  )__)     ( (_-. /(__)\  )    (  )__) 
(____/(____)\___)(____)     \___/(__)(__)(_/\/\_)(____)

"""

p = """\n\n// The Dice has six faces - 1,2,3,4,5,6
    You and Computer throw the dice simultaneously
    who got the first 6 will win the game //
    """

# computer's turn to throw the dice -->
def computer_turn():
    """computer_turn : dice number occured by computer

    Returns:
        int : any number [1-6]
    """
    dice_1 = random.randint(1, 6)
    return dice_1


# player's turn to throw the dice -->
def player_turn():
    """player_turn : dice number occured by the player

    Returns:
        int : any number [1-6]
    """
    dice_2 = random.randint(1, 6)
    return dice_2


def player_throw_dice():
    """player_throw_dice : the player to throw the dice"""
    player_throw = ""
    while player_throw not in ["t", "T"]:
        player_throw = input("\n>> Tap 'T' to thow the dice :  ").strip().lower()


def play_the_dice_game():
    """play_the_dice_game : shows the game

    Returns:
        tuple (a,b): a = dice number of computer
                     b = dice number of player
    """
    sleep(2)
    print("\n---------------------------------------------------------")

    print("\n Your Turn --> ")
    player_throw_dice()
    print(f"\n DICE is rolling . . . . . ")
    sleep(5)
    d2 = player_turn()
    print(f"\n\t\t\t\t|==> You got  -- {d2}")

    sleep(5)
    print("\n Computer's Turn --> ")
    print("\n DICE is rolling . . . . . ")
    sleep(5)
    d1 = computer_turn()
    print(f"\n\t\t\t\t|==> It's got -- {d1}")

    return (d1, d2)


def result(a, b):
    """checks who won | who got the first six"""
    if a == 6 and b != 6:
        print(
            """
         _________________
        |  COMPUTER  WON  |
         -----------------
        """
        )
        return 1
    if a != 6 and b == 6:
        print(
            """
         ____________
        |  YOU  WON  |
         ------------
        """
        )
        return 1
    if a == 6 and b == 6:
        print(
            """
         _______________
        |  ITS  A  TIE  |
         ---------------
        """
        )
        return 1


def play_game_3():
    """play_game_3 : executes all the functions for playing dice game"""
    a = play_the_dice_game()
    x = a[0]  # stores the number got by computer's dice
    z = a[1]  # stores the number got by player's dice
    b = result(x, z)  # it checks if anyone won or not

    while b != 1:
        a = play_the_dice_game()
        x = a[0]
        z = a[1]
        b = result(x, z)

    play_again_dice()


def play_again_dice():
    """ask the player if he wants to play again
    or want to change the game
    """
    player_input = ""
    while player_input not in ["y", "n", "x"]:
        player_input = (
            input(
                "\n>> Enter 'Y' to play again | 'N' to exit | or 'X' to change the game :  "
            )
            .strip()
            .lower()
        )

    if player_input == "y":
        play_game_3()
    if player_input == "x":
        play_the_games()
    else:
        print(
            """
         _______________
        |  THANKS  YOU  |
         ---------------
        """
        )
        rate_it()


# ! FISH GAME -------------------->


def fish_game_discription():
    print(
        """
    CATCH THE FISH GAME :
    -------------------
    There is a lake devided into four fish zone,
    there is a fish randomly moving to different zones
    You have 5 baits means you will get five times to play
    Each time you have to select the zone you want to throw your bait
    If you thow the bait to the same zone where the fish is, you got the fish
    ! Note : Either you catch the fish or not, you will loose the bait
    so, carefully use your bait and catch as much as fish to earn enough by
    . . selling in the market
    --------------------------------------------------------------------------
    """
    )


lake = """
                        L A K E  -  L A Y O U T
                       ------------------------- 
                 ====================================
                ||                ||                ||
                ||                ||                ||
                ||    O N E       ||     T W O      ||
                ||                ||                ||
                ||                ||                ||
                 ====================================
                ||                ||                ||
                ||                ||                ||
                ||   T H R E E    ||    F O U R     ||
                ||                ||                ||
                ||                ||                ||
                 ====================================
"""

fish = """
    
          /`·.¸
         /¸...¸`:·
     ¸.·´  ¸   `·.¸.·´)
    : © ):´;      ¸  {
     `·.¸ `·  ¸.·´\`·¸)
         `\\\´´\¸.·´
    
"""


def place_a_fish():
    """place_a_fish : this will randomly place the fish
                      in anyone of the zone

    Returns:
        str: zone number of the fish
    """
    fish_zone = random.randint(1, 4)
    return str(fish_zone)


def throw_the_bait(a):
    """throw_the_bait : ask the player to throw the bait

    Args:
        a (int): current bait number

    Returns:
        str : the zone where he has thrown the bait
    """
    throw = input(f"\n>> Which zone you want to throw the bait {a} :  ").strip()
    while throw not in ["1", "2", "3", "4"]:
        print("\n        ! Don't throw out of zone, there is no fish on the land")
        throw = input(f"\n>> Which zone you want to throw the bait {a} :  ").strip()

    return throw


def catch_it(fish, bait):
    """catch_it : checks if the fish caught or not

    Args:
        fish (str): zone where fish is
        bait (str): zone where the bait is

    Returns:
        int : returns 1 if fish and bait are in same zone, else 0
    """
    if fish == bait:
        return 1
    return 0


def fish_game():
    """fish_game : executes the functons in order to play the fish game"""
    fish_caught = 0
    baits = 1
    while baits < 6:
        fish_in = place_a_fish()
        bait_thrown = throw_the_bait(baits)
        x = catch_it(fish_in, bait_thrown)
        if x == 1:
            print(f"\n     Hoho : Got the FISH :)   {fish}")
            fish_caught += 1
        if x == 0:
            print("\n     Better luck next time :( ")
        baits += 1

    print(
        f"""
     ----------------------------------
    |  **   You catched {fish_caught} fishes   **  |
     ----------------------------------
    """
    )

    play_again_fish()


def play_again_fish():
    """ask the player if he wants to play again
    or want to change the game
    """
    print("\n\n------------------------------------------------------")
    player_input = ""
    while player_input not in ["y", "n", "x"]:
        player_input = (
            input(
                "\n>> Enter 'Y' to play again | 'N' to exit | or 'X' to change the game :  "
            )
            .strip()
            .lower()
        )

    if player_input == "y":
        fish_game()
    if player_input == "x":
        play_the_games()
    else:
        print(
            """
         _______________
        |  THANKS  YOU  |
         ---------------
        """
        )
        rate_it()


#!------ REGISTRATION :
def enter_name():
    """enter_name() : ask user to input his name

    Returns:
        str : return the entered name
    """
    Name = input("\n >>  Enter your name : ").strip()

    while Name.replace(" ", "").isalpha() == False:
        #! if you name contains character other than alphabet, enter name again
        #! until all the characters are alphabets

        print("    [x] Enter valid name ")
        Name = input("\n >>  Enter your name : ").strip()

    return Name


def enter_age():
    """enter_age : ask user to input his name

    Returns:
        str : string of his age
    """
    print("\n           Notice : Valid age to play the game 10 to 100")
    umar = input("\n >>  Enter your age : ").strip()

    while (umar.isnumeric() is False) or (int(umar) < 10 or int(umar) > 100):
        print("     [x] Enter valid age")
        umar = input("\n >>  Enter your age : ").strip()

    return umar


def enter_mobile_no():
    """enter_mobile_no : ask user to input his name
       Print errors according to:
       1: Enter 10 digit phone number
       2: If all characters are not digits [0:9]
       3: If Number does not start with any of the one digit [6,7,8 or 9]

    Returns:
        str : entered mobile number
    """
    mobile_num = input("\n >>  Enter your phone number : ").strip()

    flag = True
    while flag:
        if len(mobile_num) != 10:
            print("     [x] Enter  10  digit phone number")
            mobile_num = input("\n >>  Enter your phone number : ").strip()
        elif not mobile_num.isnumeric():
            print("     [x] Enter valid phone number")
            mobile_num = input("\n >>  Enter your phone number : ").strip()
        elif not mobile_num.startswith(("6", "7", "8", "9")):
            print(
                "     [x] Enter valid phone number that starts with 6️, 7️, 8️, or 9️"
            )
            mobile_num = input("\n >>  Enter your phone number : ").strip()
        else:
            flag = False

    return mobile_num


def email_suggestion(name):
    """email_suggestion : if user want email suggestion while registration
                          this function will print five email suggestion
                          by adding random numbers after the user name.
                          User may choose any one of them.
    Args:
        name (str): takes name as an argument to generate emails
    """

    sleep(2)
    print(
        "\n\t\t\t\t                      >> These are the five email suggestions : --> "
    )
    print("\t\t\t\t                         ------------------------------------ ")

    # ? This e_dic is used to print the serial number of the suggested emails
    # in future we can replace the key values with emoji of the same number

    e_dic = {"1": "1️", "2": "2️", "3": "3️", "4": "4️", "5": "5️"}

    for i in range(1, 6):
        num = random.randint(10, 10000)  # generate random number
        email = name + str(num) + "@gmail.com"
        sleep(1.5)
        print(f"\t\t\t\t                         {e_dic[str(i)]}  : {email}")


# Python3 code to remove whitespace
def remove(string):
    return string.replace(" ", "")


def want_email_suggestion():
    """want_email_suggestion : this function ask the user if he wants email suggestion or not"""

    # ask again if he inputs any malicious keys
    want = ""
    while want not in ["yes", "y", "n", "no"]:
        want = (
            input("\n >> Do you want email suggestion ? | YES  or  NO | :  ")
            .strip()
            .lower()
        )

    # if he wants the suggestion then ask his name and give 5 email suggestions
    if want in ["y", "yes"]:
        Name = enter_name()
        name = remove(Name)
        email_suggestion(name)


def email_in_database(Email):
    """email_in_database : this function checks that the given argumented
                           Email is present in the GameDatabase or not

    Args:
        Email (str): The email entered by the user

    Returns:
        bool : True if email found, else False
    """
    # using pandas library to read the csv file
    data = pd.read_csv("GameDatabase.csv")
    j = (
        Email + "@gmail.com"
    )  # we ask user to enter email without adding "@gmail.com" so here we add it manually
    for i in data[
        "E-mail"
    ]:  # loop through all the emails in database to check if it match with the user entered email
        if i == j:
            return True
    return False


def enter_email():
    """enter_email : ask user to enter email
       Returns Error :
       1: If it contains @ in it
       2: If email is not alphanumeric
       3: If it contains only numbers
       4: If the email is already in use
       5: If it contains whitespace

    Returns:
        str : returns Email if it pass all the errors
    """
    Email = input(
        "\n >>  Enter your email |  ! NOTE: Dont add @gmail.com | :  "
    ).strip()

    flag = True
    while flag:
        if Email.count("@") > 0:
            print("               [x] An email cant have two or more @ ")
            Email = input(
                "\n >>  Enter your email |  ! NOTE: Dont add @gmail.com | :  "
            ).strip()
        elif not Email.isalnum():
            print("                [x] Enter only alphanumeric characters")
            Email = input(
                "\n| >>  Enter your email |  ! NOTE: Dont add @gmail.com | :  "
            ).strip()
        elif Email.isnumeric():
            print("               [x] Invalid email - contains only numbers")
            Email = input(
                "\n| >>  Enter your email |  ! NOTE: Dont add @gmail.com | :  "
            ).strip()
        elif Email.isspace():
            print("              [x] Invalid email - contains whitespace")
            Email = input(
                "\n| >>  Enter your email |  ! NOTE: Don't add @gmail.com | :  "
            ).strip()
        elif email_in_database(Email):
            print("                [x] Email already in use, Try different one")
            want_email_suggestion()
            Email = input(
                "\n| >>  Enter your email |  ! NOTE: Dont add @gmail.com | :  "
            ).strip()
        else:
            flag = False

    return Email


def enter_email_without_suggestion():
    """enter_email_without_suggestion : ask user to enter email which is used during sign in process
                                        it will not give email suggestion
                                        or check if email is present in database
        Email validation check:
        1: If it contains @ in it
        2: If email is not alphanumeric
        3: If it contains only numbers
        4: If it contains whitespace

    Returns:
        str : Email entered by the user
    """
    Email = input("\n>> Enter your email |  ! NOTE: Don't add @gmail.com | :  ").strip()

    flag = True
    while flag:
        if Email.count("@") > 0:
            print("\t   [x] An email cant have two or more @ ")
            Email = input(
                "\n| >> Enter your email |  ! NOTE: Don't add @gmail.com | :  "
            ).strip()
        elif not Email.isalnum():
            print("\t   [x] Enter only alphanumeric characters")
            Email = input(
                "\n| >> Enter your email |  ! NOTE: Don't add @gmail.com | :  "
            ).strip()
        elif Email.isnumeric():
            print("\t   [x] Invalid email - contains only numbers")
            Email = input(
                "\n| >> Enter your email |  ! NOTE: Don't add @gmail.com | :  "
            ).strip()
        elif Email.isspace():
            print("\t   [x] Invalid email - contains whitespace")
            Email = input(
                "\n| >> Enter your email |  ! NOTE: Don't add @gmail.com | :  "
            ).strip()
        else:
            flag = False

    return Email


def enter_password():
    """enter_password : ask user to enter the password

    Returns:
      str: entered password after checking all the contions for errors
    """
    Password = input("\n>> Enter Password : ").strip()
    check = check_password(Password)  # check the password for the errors

    while check == 0:
        print("   [x] Enter valid password | check your errors __| ")
        Password = input("\n>> Enter Password : ").strip()
        check = check_password(Password)

    return Password


def check_password(password):
    """
    1: Minimum 8 characters.
    2: The alphabet must be between [a-z]
    3: At least one alphabet should be of Upper Case [A-Z]
    4: At least 1 number or digit between [0-9].
    5: At least 1 character from [ _ or @ or $ ].
    6: There should no spaces in the password.
    7: There should no invalid keyword in the password.
    """
    l, u, p, d, b, z = 0, 0, 0, 0, 0, 0
    s = password
    if len(s) >= 8:
        for i in s:
            if i.islower():
                l += 1
            elif i.isupper():
                u += 1
            elif i.isdigit():
                d += 1
            elif i.isspace():
                b += 1
            elif i == "@" or i == "$" or i == "_":
                p += 1
            else:
                z += 1

    if (len(s)) < 8:
        print("\t\t\t\t                   -->    Minimum 8 characters -- [X]")
    elif (len(s)) >= 8:
        if l == 0:
            print(
                "\t\t\t\t                   -->    At least one alphabet should be of Lower Case [a-z] -- [X]"
            )
        if u == 0:
            print(
                "\t\t\t\t                   -->    At least one alphabet should be of Upper Case [A-Z] -- [X]"
            )
        if d == 0:
            print(
                "\t\t\t\t                   -->    At least 1 number or digit between [0-9] -- [X]"
            )
        if b > 0:
            print(
                "\t\t\t\t                   -->    There should no spaces in the password -- [X]"
            )
        if p == 0:
            print(
                "\t\t\t\t                   -->    At least 1 character from [ _ or @ or $ ] -- [X]"
            )
        if z > 0:
            print(
                "\t\t\t\t                   -->    Invalid keyword persent in the password -- [X]"
            )

    if (
        l >= 1
        and u >= 1
        and p >= 1
        and d >= 1
        and b == 0
        and z == 0
        and l + p + u + d == len(s)
    ):
        return 1  # returns 1 if it pass all the conditions
    else:
        return 0  # else return 0


def generate_captcha():
    """generate_captcha : it generate a 4 character captcha code randomly
                          from ascii letters and numbers

    Returns:
        str : captcha code
    """
    # use the string libraray to form the list of collection of lower and upper case letters
    letters = list(string.ascii_letters)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    captcha_lst = letters + numbers

    captcha = ""
    for i in range(4):
        captcha += random.choice(captcha_lst)

    return captcha


def print_captcha(captcha):
    """print_captcha : it prints the generated captcha code by using some of the characters emojis

    Args:
        captcha (str): takes generated captcha string as an argument

    Returns:
        str : captcha code with some emojis
    """
    # i created this dictionary to print some emojis but the exe does not support it,
    # in future the values can be replaced by the emojis with the same string name
    c_dic = {
        "0": "0️",
        "1": "1️",
        "2": "2️",
        "3": "3️",
        "4": "4️",
        "5": "5️",
        "6": "6️",
        "7": "7️",
        "8": "8️",
        "9": "9️",
        "A": "A",
        "B": "B",
        "P": "P",
        "O": "O",
        "M": "M",
    }

    c = ""
    # loop through the generated captcha code and find if any of the character has an emoji
    # if that character has an emoji in c_dic than add that emoji in c ' otherwise add that character itself
    for i in captcha:
        if i in c_dic:
            c = c + " " + c_dic[i]
        else:
            c = c + "   " + i
    return c


def enter_captcha():
    """enter_captcha : ask user to enter captcha seen at the console

    Returns:
        str : entered captcha code
    """
    k = input(" >>  Enter the captcha : ").strip()
    return k


def check_captcha():
    """check_captcha : this function will check
    is the entered captcha equal to the generated captcha ?
    """
    gen_c = generate_captcha()
    print_code = print_captcha(gen_c)
    print(f"\n\n >>  Captcha code is : {print_code}")
    ent_c = enter_captcha()
    while gen_c != ent_c:
        gen_c = generate_captcha()
        print_code = print_captcha(gen_c)
        print(f"\n\n >>  Captcha code is : {print_code}")
        ent_c = enter_captcha()


def email_guidlines():
    print(
        """
                                                     ------------------------------------------------------------------------
                                                    |                    ! : G U I D L I N E S : !                           |
                                                    |          Primary conditions for email validation:                      |
                                                    |          1: NOTE: Dont't add @gmail.com - we will do it for you        |
                                                    |          2: Should be aplhabetic or alphanumeric                       |
                                                    |          3: Don't add any special characters - even {'@'}              |
                                                    |          4: Should not contain space between the characters            |
                                                    |          5: If the email is already registered, then try with          |
                                                    |             another email or rerun the program and go for signin       |
                                                     ------------------------------------------------------------------------
        """
    )


def guidlines():
    """guidlines : this function will show the conditions for password validation
    during the registration process so that user input a correct
    format for password
    """
    print(
        """
                                                     ------------------------------------------------------------------------
                                                    |                    ! : G U I D L I N E S : !                           |
                                                    |            Primary conditions for password validation:                 |
                                                    |            1: Minimum 8 characters.                                    |
                                                    |            2: The alphabet must be between [a-z]                       |
                                                    |            3: At least one alphabet should be of Upper Case [A-Z]      |
                                                    |            4: At least 1 number or digit between [0-9].                |
                                                    |            5: At least 1 character from [ _ or @ or $ ].               |
                                                    |            6: There should no spaces in the password.                  |
                                                     ------------------------------------------------------------------------
        """
    )


def registration():
    """registration : This function does the registration process
    asking the user to enter his informations
    and after the process append the same informations
    to the game databse
    INFORMATIONS :
    Name -- Age -- Mobile_No -- Email -- Password
    """
    sleep(2)
    print(
        "\n-----------------------------------------------------------------------------\n"
    )
    print("                   || +  R E G I S T R A T I O N  + ||")
    print("\t  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
    sleep(2)
    name = enter_name()

    sleep(1)
    age = enter_age()

    sleep(1)
    mobile_no = enter_mobile_no()

    sleep(2)
    email_guidlines()
    sleep(2)
    email = enter_email()

    sleep(2)
    guidlines()
    sleep(2)
    password = enter_password()

    sleep(1)
    print(
        "\n\t\t\t\t\t NOTE : While entering captcha code do not enter the space between the characters"
    )
    check_captcha()

    gmail = email + "@gmail.com"
    with open("GameDatabase.csv", "a") as data:
        data.write(f"\n{name},{age},{mobile_no},{gmail},{password}")

    sleep(3)
    print(
        """
     ______________________
    |  REGISTRATION  DONE  |
     ----------------------
    """
    )


#!------- S I G N   I N ------
def check_for_password(email, password):
    """check_for_password : check the email's password is equal
                            to the password entered by the user

    Args:
        email (str): email of the registered user
        password (_type_): password entered by the user

    Returns:
        bool : True - if password matches, else False
    """
    # using Pandas library to bring out the password of the registered email
    data = pd.read_csv("GameDatabase.csv", index_col="E-mail")
    pswd = data.loc[email, "Password"]
    if pswd == password:
        return True
    return False


def ask_for_reg():
    """ask_for_reg : asking the user if he wants to register himself or not
    if he wants to register than jump into the registration page
    and after the process ask him to signin
    """
    while True:
        ask = (
            input(
                "\n>> Do you want to register yourself with your email | Yes  or  No | : "
            )
            .strip()
            .lower()
        )
        # if he wants to register himself then go to registration process and then go for signin process
        if ask in ["y", "yes"]:
            registration()
            ask_for_signin()
            break
        elif ask in ["n", "no"]:
            print("\n----------------------------------------------------------------")
            print("             >>>  Thank you for visiting  <<<")
            print("----------------------------------------------------------------")
            exit_the_game()
        else:
            pass


def ask_for_signin():
    """ask_for_signin : asking the user if he wants to sign in or not"""
    while True:
        ask = input("\n>> Do you want to sign in | Yes   or  No  | : ").strip().lower()
        if ask in ["y", "yes"]:
            sign_in()
            break
        elif ask in ["n", "no"]:
            print("\n>> You have to SignIn before playing the game")
            sleep(3)
            print("\n-----------------------------------------------------------------")
            print("             >>>  Thank you for visiting  <<<")
            print("-----------------------------------------------------------------")
            exit_the_game()
        else:
            pass


def otp():
    """otp : this function generates random 4 digits number as otp
             and write it to a file

    Returns:
        str : string of the generated number
    """
    Otp = random.randint(1000, 9999)
    with open("GameOneTimePin.txt", "w") as otpFile:
        otpFile.write(str(Otp))
    return str(Otp)


def enter_otp():
    """enter_otp : ask user to enter the otp

    Returns:
        str : string of the number entered
    """
    o = input("\n>> Enter  OTP  :  ").strip()
    while len(o) > 4:
        print("    [x] Invalid otp -- Enter 4 digit otp")
        o = input("\n>> Enter  OTP  :  ").strip()
    return o


def check_otp(gen_otp, en_otp):
    """check_otp : this function will check
                   is entered otp is equal to generated otp

    Args:
        gen_otp (str): otp generated by otp() function
        en_otp (_type_): otp entered by the user

    Returns:
        bool : True if both are equal
    """
    if gen_otp == en_otp:
        return True
    else:
        return False


def show_password(email):
    """show_password : this function will show the user
                       password in the GameYourPassword.txt file

    Args:
        email (str): the email of the user (must have --@gmail.com)
    """
    data = pd.read_csv("GameDatabase.csv", index_col="E-mail")
    pswd = data.loc[email, "Password"]
    with open("GameYourPassword.txt", "w") as f:
        f.write(pswd)


def forgot_pass(email):
    """forgot_pass : This function will process
                     the steps for forgot password

    Args:
        email (str): works on the entered email
    """
    print("\n>> * Sending OTP ... to GameOneTimePin.txt file in your game directory ")
    generated_otp = otp()
    sleep(6)
    print("\n>> ** OTP sent ")
    enter_OTP = enter_otp()
    if check_otp(generated_otp, enter_OTP):
        show_password(email)
        sleep(5)
        print("\n>> Password sent to GameYourPassword.txt file in your game directory ")
    else:
        print("\n>> ** Wrong OTP -- Don't try to get access of someones else account")


def sign_in():
    """sign_in : SIGN IN process -->
    1: First ask the user to enter his email
    2: Check if email is in the database or not
    3: If email in database than enter password
    4: If password is correct than play game
    5: If password is incorrect than you can try three more times
    6: If any time password matches than you will play the game
    7: Else ask for forgot password
    """
    sleep(2)
    print(
        "\n-----------------------------------------------------------------------------\n"
    )
    print("                    || >>   S I G N   I N   << || ")
    print("\t   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")

    mail = enter_email_without_suggestion()
    if email_in_database(mail):
        # if email found in the registered database than ask for password
        password = enter_password()
        gmail = mail + "@gmail.com"
        if check_for_password(gmail, password):
            sleep(2)
            print("\n{+}  Password Correct")
            play_the_games()
        else:
            sleep(2)
            print(
                "\n   [X] Password Incorrect - Try again ( ! NOTE: You Can Try Only Three More Times)"
            )
            a = 0
            while a < 3:
                password = enter_password()
                gmail = mail + "@gmail.com"
                if check_for_password(gmail, password):
                    sleep(2)
                    print("\n{+}  Password Correct")
                    play_the_games()
                    break
                else:
                    sleep(2)
                    print("\n   [X] Password Incorrect")
                    a += 1

            if a == 3:
                forget = ""
                while forget not in ["y", "yes", "n", "no"]:
                    forget = (
                        input(
                            "\n>> Have you forgot your password > Press 'Y' to see your password or 'N' to exit :  "
                        )
                        .strip()
                        .lower()
                    )
                gmail = mail + "@gmail.com"
                if forget in ["y", "yes"]:
                    forgot_pass(gmail)
                    ask_for_signin()
                elif forget in ["n", "no"]:
                    ask_for_signin()

    else:
        print("\n >> Email not found , --> First register with your email ")
        ask_for_reg()


def readme():
    """readme : this is the readme section shows some instructions before playing the game"""
    print(
        """
          
----------------------------------------------------------------------------
                              ||   R E A D M E   ||
                              
                    When the game ask for your response in Yes or No -->
                    You can enter any one of these :
                    1) [y, Y]  for -- Yes
                    2) [n, N]  for -- No
                                &
                    Numbers [integers] while playing game
----------------------------------------------------------------------------
          
          """
    )


#
def play_the_games():
    """play_the_games : this function ask which game you want to play"""
    sleep(2)
    print(
        "\n\n Now play some games from the list ! NOTE -- enter the serial number of the game to play it "
    )
    sleep(2)
    print(
        """
        ||||||||||||||||||||||||||||||||||||||||||||||||||
        |           --------------------------           |
        |             ///    G A M E S    ///            |
        |           --------------------------           |
        |                                                |
        |         1 --> ROCK | PAPER | SCISSORS          |
        |         2 --> GUESS THE NUMBER                 |
        |         3 --> DICE GAME                        |
        |         4 --> CATCH THE FISH                   |
        |                                                |
         ------------------------------------------------
        """
    )
    game_choose = ""
    while game_choose not in ["1", "2", "3", "4"]:
        game_choose = input("\n>> Which game do you want to play ? :  ").strip()

    if game_choose == "1":
        play_the_game_1()
    if game_choose == "2":
        sleep(1)
        print(gg)
        sleep(1.5)
        play_the_game_2()
    if game_choose == "3":
        sleep(1)
        print(dd)
        sleep(2)

        print(p)
        sleep(2)

        play_game_3()
    if game_choose == "4":
        sleep(2)
        fish_game_discription()
        sleep(4)
        print(lake)
        sleep(3)
        fish_game()
    else:
        pass
    # TODO Add More Games


dart = """
                        .-;;;-.
                       / .===. \\
                       \/ 6 6 \/
                       ( \___/ )
          _________ooo__\_____/_____________
         /                                  \\
        |    DEVELOPER :                     |
        |         -- ABHINAV RAJ       :)    |
        |    BUG HUNTER :                    |
        |         -- ANURAG RANA       :)    |
        |                                    |
         \______________________ooo_________/
                       |  |  |
                       |_ | _|
                       |  |  |
                       |__|__|
                       /-'Y'-\\
                      (__/ \__)

"""


def exit_the_game():
    """exit_the_game : this function will exit the code"""
    sleep(2)
    print(dart)
    while True:
        e = input("\n >>  Enter 'E' to exit the game : ").strip().lower()
        if e == "e":
            exit()
        else:
            print("\n          [x]  Enter 'E' to exit")


def player_play_the_game():
    """player_play_the_game : this function ask the user if he is a new player or not
    1: If you are a new user ask for registration
    2: If you are alredy registered user than go for SignIn
    """
    print(pg)

    sleep(2)
    readme()

    sleep(3)
    user = ""
    while user not in ["y", "yes", "n", "no"]:
        user = input("\n>> Are you a new user | Yes   or  No  | :  ").strip().lower()

    if user in ["y", "yes"]:
        print("\n --> At first you have to register yourself with your email")
        sleep(1.5)
        ask_for_reg()
    else:
        ask_for_signin()


# * : LETS PLAY THE GAME -->
player_play_the_game()
