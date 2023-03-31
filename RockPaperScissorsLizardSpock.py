import os
import random

def titleASCII():
    print("____ ____ ____ __ _   ____ ___  ____ ____ ____   ___  ____ ____ ___  ___  ____ ____ ___  ")
    print("| . \|   || __\| V \  | . \|  \ | . \| __\| . \  | _\ | __\|___\| _\ | _\ |   || . \| _\ ")
    print("|  <_| . || \__|  <_  | __/| . \| __/|  ]_|  <_  [__ \| \__| /  [__ \[__ \| . ||  <_[__ \ ")
    print("|/\_/|___/|___/|/\_/  |/   |/\_/|/   |___/|/\_/  |___/|___/|/   |___/|___/|___/|/\_/|___/")
    print("__   ____ ___  ___  ____ ___    ___  __   ___    ___  ____ ____ ____ __ _                ")
    print("| |  |___\|_ \ |  \ | . \|  \   |  \ | \|\|  \   | _\ | . \|   || __\| V \               ")
    print("| |__| /  | __]| . \|  <_| . \  | . \|  \|| . \  [__ \| __/| . || \__|  <_               ")
    print("|___/|/   |___/|/\_/|/\_/|___/  |/\_/|/\_/|___/  |___/|/   |___/|___/|/\_/")

def menu():
    titleASCII()
    print("\nWelcome to Rock, Paper, Scissors, Lizard, and Spock Game (EXTENDED)\n")
    print(">> [1] Player VS Computer")
    print(">> [2] Player VS Player")
    print(">> [3] [NEW!] Powerup Game Mode")
    print(">> [4] How to Play")
    print(">> [99] EXIT\n")
    userChoice = False
    while (userChoice == False):
        choice = str(input("Select a Choice: e.g. '1': "))
        if choice == '1':
            userChoice = True
            vsComputer()
        elif choice == '2':
            userChoice = True
            vsPlayer()
        elif choice == '3':
            userChoice = True
            powerUp()
        elif choice == '4':
            userChoice = True
            how2Play()
        elif choice == '99':
            userChoice = True
            print("Thank you for playing!")
            exit()
        else:
            print("Invalid Choice. Please Try again.")

def graphicChoice(P1choice, P2choice):
    if P1choice == "rock":
        rock()
    elif P1choice == "scissors":
        scissors()
    elif P1choice == "paper":
        paper()
    elif P1choice == "lizard":
        lizard()
    elif P1choice == "spock":
        spock()
    vs()
    if P2choice == "rock":
        rock()
    elif P2choice == "scissors":
        scissors()
    elif P2choice == "paper":
        paper()
    elif P2choice == "lizard":
        lizard()
    elif P2choice == "spock":
        spock()


def vsComputer():
    print("\nWelcome to Player vs Computer Game Mode!")
    userPlay = True
    P1score = 0
    P2score = 0
    round = 1
    while (userPlay == True):
        gameProceed = False
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        print("___________________________________________")
        print(f"[SCORE] P1 = {P1score} || CP = {P2score}")
        print(f"[ROUND {round}]")
        print("___________________________________________")

        user_choice = str(input("Please choose rock, paper, scissors, lizard, or spock [type 'exit' to quit]: ").lower())

        if user_choice == "exit":
            userPlay = False
            menu()
        elif user_choice not in choices:
            print("Invalid choice. Please try again.")
        elif user_choice in choices:
            gameProceed = True

        if gameProceed == True:

            computer_choice = random.choice(choices)
            print("Computer chose: ", computer_choice)

            if user_choice == computer_choice:
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                P2score += 1
                print("It's a tie!")

            elif user_choice == "rock" and computer_choice == "scissors":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "paper" and computer_choice == "rock":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "scissors" and computer_choice == "paper":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "rock" and computer_choice == "lizard":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "lizard" and computer_choice == "spock":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "spock" and computer_choice == "rock":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "lizard" and computer_choice == "paper":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "paper" and computer_choice == "spock":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "scissors" and computer_choice == "lizard":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            elif user_choice == "spock" and computer_choice == "scissors":
                graphicChoice(user_choice, computer_choice)
                P1score += 1
                print("You won!")
            else:
                graphicChoice(user_choice, computer_choice)
                P2score += 1
                print("Computer won.")
            round +=1

def vsPlayer():
    print("\nWelcome to Player vs Player Game Mode!")
    userPlay = True
    P1score = 0
    P2score = 0
    round = 0
    while (userPlay == True):
        gameProceed = False
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        print("___________________________________________")
        print(f"[SCORE] P1 = {P1score} || P2 = {P2score}")
        print(f"[ROUND {round}]")
        print("___________________________________________")

        user1_choice = str(
            input("Please choose rock, paper, scissors, lizard, or spock [type 'exit' to quit]: ").lower())
        os.system('cls')
        if user1_choice != "exit":
            user2_choice = str(
                input("Please choose rock, paper, scissors, lizard, or spock [type 'exit' to quit]: ").lower())
        os.system('cls')

        if user1_choice == "exit":
            userPlay = False
            menu()
        elif user1_choice and user2_choice not in choices:
            print("Invalid choice. Please try again.")
        elif user1_choice and user2_choice in choices:
            gameProceed = True

        if gameProceed == True:

            if user1_choice == user2_choice:
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                P2score += 1
                print("It's a tie!")

            elif user1_choice == "rock" and user2_choice == "scissors":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "paper" and user2_choice == "rock":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "scissors" and user2_choice == "paper":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "rock" and user2_choice == "lizard":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "lizard" and user2_choice == "spock":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "spock" and user2_choice == "rock":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "lizard" and user2_choice == "paper":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "paper" and user2_choice == "spock":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "scissors" and user2_choice == "lizard":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            elif user1_choice == "spock" and user2_choice == "scissors":
                graphicChoice(user1_choice, user2_choice)
                P1score += 1
                print("Player 1 won!")
            else:
                graphicChoice(user1_choice, user2_choice)
                P2score += 1
                print("Player 2 won.")
            round += 1

def powerUp():
    print("\nWelcome to [Power Up!] Player vs Computer Game Mode!")
    userPlay = True
    round = 1

    #p1 status
    P1hp = 10
    P1poisonStatus = False
    P1poisonCounter = 0

    #computer status
    CPhp = 10
    P2poisonStatus = False
    P2poisonCounter = 0

    #game proper
    while (userPlay == True):
        #makes sure HP never goes less than zero
        if P1hp < 0:
            P1hp = 0
        if CPhp < 0:
            CPhp = 0

        if P1hp == 0 or CPhp == 0:
            print("Round is over.")
            if P1hp > CPhp:
                print("You win.")
            elif CPhp > P1hp:
                print("Computer wins.")
            print("___________________________________________")
            print("GAME SUMMARY:")
            print(f"[HP] P1 = {P1hp}/10 || CP = {CPhp}/10")
            print(f"[ROUND {round}]")
            print("___________________________________________")
            userEndSelect = False
            while(userEndSelect == False):
                choiceEnd = str(input("Would you like to play again? [type 'exit' or 'again']: "))
                if choiceEnd == "exit":
                    userEndSelect = True
                    menu()
                if choiceEnd == "again":
                    userEndSelect = True
                    round = 1
                    #resetP1status
                    P1hp = 10
                    P1poisonStatus = False
                    P1poisonCounter = 0
                    #resetP2status
                    CPhp = 10
                    P2poisonStatus = False
                    P2poisonCounter = 0
                else:
                    print("Invalid Choice. Please try again.")
        else:
            gameProceed = False
            choices = ["rock", "paper", "scissors", "lizard", "spock"]
            powerUps = ["SHIELD", "HEAL", "POISON", "SWITCH"]
            print("___________________________________________")
            print(f"[HP] P1 = {P1hp}/10 || CP = {CPhp}/10")
            print(f"[ROUND {round}]")
            print("___________________________________________")

            user_choice = str(input("Please choose rock, paper, scissors, lizard, or spock [type 'exit' to quit]: ").lower())

            if user_choice == "exit":
                userPlay = False
                menu()
            elif user_choice not in choices:
                print("Invalid choice. Please try again.")
            elif user_choice in choices:
                gameProceed = True

            if gameProceed == True:

                computer_choice = random.choice(choices)
                P1Powerup = random.choice(powerUps)
                CPPowerup = random.choice(powerUps)

                print(f"Your random powerup for this round is {P1Powerup}")
                print("Computer chose: ", computer_choice)
                print(f"Computer's random powerup for this round is {CPPowerup}")

                if P1Powerup == "POISON":
                    if P2poisonStatus == False:
                        P2poisonStatus = True
                elif P1Powerup == "SHIELD":
                    P1prevHP = P1hp
                elif P1Powerup == "SWITCH":
                    graphicChoice(user_choice, computer_choice)
                    print("A switch powerup has been applied to Player 1!")
                    temp = user_choice
                    user_choice = computer_choice
                    computer_choice = temp

                if CPPowerup == "POISON":
                    if P1poisonStatus == False:
                        P1poisonStatus = True
                elif CPPowerup == "SHIELD":
                    CPprevHP = CPhp
                elif CPPowerup == "SWITCH":
                    graphicChoice(user_choice, computer_choice)
                    print("A switch powerup has been applied to computer!")
                    temp = computer_choice
                    computer_choice = user_choice
                    user_choice = temp


                if user_choice == computer_choice:
                    graphicChoice(user_choice, computer_choice)
                    print("It's a tie!")

                elif user_choice == "rock" and computer_choice == "scissors":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "paper" and computer_choice == "rock":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "scissors" and computer_choice == "paper":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "rock" and computer_choice == "lizard":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "lizard" and computer_choice == "spock":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "spock" and computer_choice == "rock":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "lizard" and computer_choice == "paper":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "paper" and computer_choice == "spock":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "scissors" and computer_choice == "lizard":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                elif user_choice == "spock" and computer_choice == "scissors":
                    graphicChoice(user_choice, computer_choice)
                    CPhp -= 1
                    print("You won!")
                else:
                    graphicChoice(user_choice, computer_choice)
                    P1hp -=1
                    print("Computer won.")

                if P1Powerup == "SHIELD":
                    if P1prevHP > P1hp:
                        print("SHIELD powerup activated! You take no damage.")
                        P1hp += 1
                    else:
                        print("You have not been damaged, SHIELD powerup has no effect.")

                if CPPowerup == "SHIELD":
                    if CPprevHP > CPhp:
                        print("Computer SHIELD powerup activated! They take no damage.")
                        CPhp += 1
                    else:
                        print("Computer has not been damaged, SHIELD powerup has no effect.")

                if P1poisonStatus == True:
                    if P1poisonCounter <= 2:
                        print("You have been poisoned! Your HP decreases by 0.5 point.")
                        P1poisonCounter += 1
                        P1hp -= 0.5
                    else:
                        print("Your poison status has been lifted!")
                        P1poisonCounter = 0
                        P1poisonStatus = False

                if P2poisonStatus == True:
                    if P2poisonCounter <= 2:
                        print("Computer has been poisoned! Their HP decreases by 0.5 point.")
                        P2poisonCounter += 1
                        CPhp -= 0.5
                    else:
                        print("Computer poison status has been lifted!")
                        P2poisonCounter = 0
                        P2poisonStatus = False

                if P1Powerup == "HEAL":
                    if P1hp >= 10:
                        P1hp = 10
                        print("HEAL powerup activated! Max HP Exceeded, no effect!")
                    else:
                        print("HEAL powerup activated! You gain 0.5 HP point")
                        P1hp += 0.5
                if CPPowerup == "HEAL":
                    if CPhp >= 10:
                        CPhp = 10
                        print("Computer HEAL powerup activated! Max HP Exceeded, no effect!")
                    else:
                        print("Computer HEAL powerup activated! They gain 0.5 HP point")
                        CPhp += 0.5


                round +=1

def how2Play():
    print("_________________________________________________________________________")
    print("HOW TO PLAY?\n")
    print("Here are the rules of this game:")
    print("> scissors cuts paper")
    print("> paper covers rock")
    print("> rock smashes lizard")
    print("> lizard poisons spock")
    print("> spock smashes scissors")
    print("> scissors decapitates lizard")
    print("> lizard eats paper")
    print("> paper disproves spock")
    print("> spock vaporizes rock")
    print("> rock smashes scissors\n\n")

    print("GAME MODES:\n")
    print("-------Player VS Computer:")
    print("       > Each round, the player will be the first to select between rock, paper, scissors, lizard, and spock.")
    print("       > The computer will make a random choice.")
    print("       > The player's and computer's choices will be compared according to the game rules, and whoever wins will receive one point.")
    print("\n\n-------Player VS Player:")
    print("       > Each round,Player 1 and Player 2 will enter their selections sequentially.")
    print("       > The player 1's and player 2's choices will be compared according to the game rules, and whoever wins will receive one point.")
    print("       > Whoever wins will receive one point.")
    print("\n\n-------Powerup Game Mode:")
    print("       > The game will start with both player and computer having a 10 HP.")
    print("       > Each round, the player will be the first to select between rock, paper, scissors, lizard, and spock.")
    print("       > The computer will make a random choice.")
    print("       > A random powerup will be generated. Random powerups can be shield, switch, poison, or heal.")
    print("       [1] Shield -> Allows the player or computer to block HP damage if they lose.")
    print("       [2] Poison -> Allows the player or computer to poison their opponent, causing them to lose 0.5 HP. The poison will be lifted after three rounds.")
    print("       [3] Switch -> Allows the player or computer to switch move with their opponent.")
    print("       [4] Heal ---> Restores 0.5 HP.")
    print("       > The player's and computer's choices will be compared according to the game rules, and whoever loses will receive 0.5 HP deduction.")
    print("       > The first one to have 0 HP loses and the remaining player will win.")
    print("_________________________________________________________________________")
    print("[1] Back to Menu")
    print("[99] Exit\n")
    userChoice = False
    while (userChoice == False):
        choice = str(input("Select a Choice (e.g. '1'): "))
        if choice == '1':
            userChoice = True
            print("_________________________________________________________________________")
            menu()
        elif choice == '99':
            userChoice = True
            print("_________________________________________________________________________")
            print("Thank you for playing!")
            return 0
        else:
            print("_________________________________________________________________________")
            print("Invalid Choice. Please Try again.")

def vs():
    print("\t_  _ ___  ")
    print("\t|| |\| _\ ")
    print("\t||/ /[__ \ ")
    print("\t|__/ |___/")

def rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

def paper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

def scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

def lizard():
    print("""
    
                           )/_
                 _.--..---"-,--c_
            \L..'           ._O__)_
    ,-.     _.+  _  \..--( /        
      `\.-''__.-' \ (     \_     
        `'''       `\__   /\
                    ')
    """)

def spock():
    print("""
                    _
                   / )
                  / /    _
        _        / /    / )
       ( `.     / /-.  / /
        `\ \   / // /`/ /
          ; `-`  (_/ / /
          |       (_/ /
          \          /
           )       /`
          /      /
          """)
menu()