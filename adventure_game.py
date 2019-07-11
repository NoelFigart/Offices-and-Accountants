import time
import random

# Lists of items, values for the stats for charisma, luck, and knowledge
items = []
stat_values = ["low", "high"]
stat_knowledge = []
stat_luck = []
stat_charisma = []


# Pauses between lines of text to allow for reading speed
def print_pause(text_print):
    time.sleep(2)
    print(text_print)


# If an incorrect door is chosen, redirects player.
def bad_door():
    print_pause("You must enter a 1, 2, or 3")
    doors()


# game introduction
def intro():
    print_pause("You are a dragon named Gleep.\n")
    print_pause("Today, you have come to your first role-playing game.\n")
    print_pause("Your game master is a Troll named Jade.\n")
    print_pause("Your other companions are an Ogre named Nutt,who plays a \n"
                "secretary and a Goblin named Stinky, who plays an \n"
                "IRS auditor.\n\n")
    print_pause("Because you are new, you will play\n"
                "an accountant named Grimble.\n\n")


# player rolls for Charisma -- values either low or high.
def charisma_stats():
    print_pause("You need to roll for your character\n "
                "strengths and weaknesses\n")
    print_pause("First, you roll for Charisma.\n")
    response = input("Press Y to roll.\n").lower()
    charisma = random.choice(stat_values)
    stat_charisma.append(charisma)
    while True:
        if "y" in response:
            if charisma == "low":
                print_pause("Bummer, you have low Charisma\n")
                break
            else:
                print_pause("Rock!  You have high Charisma!\n")
                break
        else:
            print_pause("You have to press yes!\n")
            response = input("Press Y to roll.\n").lower()


# player rolls for knowledge.  Value will be low or high.


def knowledge_stats():
    print_pause("Now, roll for Knowledge.\n")
    response = input("Press Y to roll.\n").lower()
    knowledge = random.choice(stat_values)
    stat_knowledge.append(knowledge)
    while True:
        if "y" in response:
            if knowledge == "low":
                print_pause("Oh dear, you have low Knowledge.\n")
                break
            else:
                print_pause("Go you!  You have high Knowledge!\n")
                break
        else:
            print_pause("You have to press yes!\n")
            response = input("Press Y to roll.\n").lower()


# player rolls for luck.  Value will be low or high.
def luck_stats():
    print_pause("Time to roll for Luck.\n")
    response = input("Press Y to roll.\n").lower()
    luck = random.choice(stat_values)
    stat_luck.append(luck)
    while True:
        if "y" in response:
            if luck == "low":
                print_pause("Bad luck.  Low luck for you.\n")
                break
            else:
                print_pause("Fantastic!  You have high luck!\n")
                break
        else:
            print_pause("You have to press yes!\n")
            response = input("Press Y to roll.\n").lower()


# Explains game goal
def game_begin():
    print_pause("Now that you have rolled your stats, let the game begin!\n")
    print_pause("You are an accountant named Grimble.\n"
                "Your goal: To get your client's tax paperwork filled out \n"
                "and submitted to the auditor.\n")


# Allows player to choose a door to go into.
def doors():
    response = input("You see three doors.\n\n"
                     "Door 1 is of frosted glass, and you hear the sound of\n"
                     "typing from inside.\n\n"
                     "Door 2 is a blank wooden door.\n"
                     "There are faint sounds of someone singing ragtime.\n\n"
                     "Door 3 is a metal door painted battleship grey.\n"
                     "What door do you choose?\n\n").lower()
    if response == "1":
        goal_one()
    elif response == "2":
        goal_two()
    elif response == "3":
        goal_three()
    else:
        bad_door()


# Goal One -- Get blank forms from secretary.
# High Charisma is a win. Saving throw is high luck.


def goal_one():
    if "forms" in items:
        print_pause("The secretary sighs and says, \n"
                    "'Don't you have work to do?'\n")
        print_pause("You leave the office, chagrined.\n")
        doors()
    else:
        print_pause("A woman at the desk stops typing and frowns at you.\n\n"
                    "'Yes?' she asks and waits.\n")
        if "high" in stat_charisma:
            print_pause("As she looks at you, her frown fades.\n"
                        "'Certainly, Mr. Grimble.  Here's your forms.'\n"
                        "She hands you a thick stack of forms.\n")
            items.append("forms")
            doors()
        else:
            print_pause("The secretary gives you a long, cool glare\n")
            answer_1 = input("Do you want to ask again? Y or N\n").lower()
            if "y" in answer_1:
                if "high" in stat_luck:
                    print_pause("The secretary hands you the forms and\n"
                                "rolls her eyes.\n")
                    items.append("forms")
                    doors()
                else:
                    print_pause("Bad luck.  She won't help you. Game over.\n")
            else:
                print_pause("You leave the office and disappaear \n"
                            "in a puff of smoke.\n")
                replay()


# Goal Two - Fill out blank forms
# High Knowlege is a win.  Saving throw is high luck

def goal_two():
    if "completed forms" in items:
        print_pause("The frog gives you a LOOK and points to the door.\n")
        print_pause("You leave your office to find the Auditor.\n")
        doors()
    else:
        if "forms" in items:
            if "high" in stat_knowledge:
                print_pause("With lightning speed, you complete the forms.\n")
                print_pause("Feeling triumphant, you leave the office.\n")
                items.append("completed forms")
                doors()
            else:
                print_pause("Reading the form, you realize you cannot \n"
                            "understand your client's chicken scratch.\n")
                print_pause("You wonder if anyone can help.\n")
                answer_2 = input("Do you ask the frog for help? Y/N\n").lower()
                if "y" in answer_2:
                    if "high" in stat_charisma:
                        print_pause("Michigan J. Frog, only you can save me.\n"
                                    "Help me please!\n")
                        print_pause("The frog elbows you aside, completing\n"
                                    "the forms in record time.\n")
                        items.append("completed forms")
                        doors()
                    else:
                        print_pause("'Well, dummy, do you know the answer?'\n"
                                    "you ask with a sneer.\n")
                        print_pause("The frog grabs a cane and \n"
                                    "beats you senseless.\n")
                        print_pause("You lose.  Game over.\n")
                        replay()
        else:
            print_pause("A frog sits on the desk beside the plaque\n"
                        "JR Grimble and ribbits with great solemnity\n.")
            print_pause("You exit the room.\n\n")
            doors()


# Goal Three -- Give completed forms to auditor
# High luck is a win.  Saving throw is high knowledge.


def goal_three():
    if "completed forms" in items:
        if "high" in stat_luck:
            print_pause("The Auditor jumps up from his cell phone.\n")
            print_pause("With a cry of joy, he grabs the forms.\n")
            print_pause("Congratulations, Grimble!  You made the deadline!\n")
            print_pause("You win!\n")
            replay()
        else:
            print_pause("The Auditor ignores you, playing with his phone.\n")
            response = input("Do you want to try again? Y/N\n")
            if "y" in response:
                if "high" in stat_knowledge:
                    print_pause("You have had the Auditor ignore you before,\n"
                                "and you are prepared.\n")
                    print_pause("You take an airhorn from your pocket and\n"
                                "blow it loudly.")
                    print_pause("The auditor jumps, dropping his phone.\n")
                    print_pause("With a glare the Auditor grabs your forms.\n")
                    print_pause("'Fine, Grimble,' the Auditor says. \n"
                                "'You got them in on time.'\n")
                    print_pause("You leave the office happily. You won.\n")
                    replay()
                else:
                    print_pause("'Sorry, Grimble. It's after five.\n"
                                "You're too late.\n")
                    print_pause("Sadly, you leave the office, defeated.\n")
                    replay()
    else:
        print_pause("The door will not open. A digital sign asks\n"
                    "DO YOU HAVE THE CORRECT FORMS CORRECTLY FILLED OUT?\n")
        doors()


# Prompts the user to replay the game and thanks the user if they do not.


def replay():
    response = input("Would you like to play again? Y/N?\n").lower()
    if "y" in response:
        stat_charisma.clear()
        stat_knowledge.clear()
        stat_luck.clear()
        items.clear()
        play_game()
    else:
        print_pause("Thank you for playing Offices and Accountants!")


# All functions needed to play the game.
def play_game():
    intro()
    charisma_stats()
    knowledge_stats()
    luck_stats()
    game_begin()
    doors()
    replay()


play_game()
