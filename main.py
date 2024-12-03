import random

def userChoice():
    """ This function will prompt the user to enter their choice """

    userchoice = input('Please enter your choice: rock, paper, or scissors: ')

    if userchoice != 'rock' and userchoice != 'paper' and userchoice != 'scissors':

        print("Please type : rock, paper or scissors")
        userChoice()
    else:

        print("You choose : " + userchoice)

    return userchoice


def computerChoice():
    """ This function will randomly select a choice for the computer """

    computechoice = random.choice(['rock', 'paper', 'scissors'])

    return computechoice


def game():
    """This function compares the user's choice with the computer's choice and determines the winner. If the returned result is 1, players finished on equality. If the returned result is 2, computer won. If the returned result is 3, the user won and if the returned result us 4, the game ran to an error """


    computer = computerChoice()
    user = userChoice()
    result = 0



    if user == computer:

        print("The computer choice is : " + computer)
        print("Both players made the same choice. Let's restart the game.")
        game()


    elif computer == "rock" and user == "scissors" or computer == "paper" and user == "rock" or computer == "scissors" and user == "paper":

        print("The computer choice is : " + computer)
        print("Computer won!")


    elif user == "rock" and computer == "scissors" or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":

        print("The computer choice is : " + computer)
        print("You won!")

    else:

        print("The game ran into an error let's restart the game. Please report this error to github.com/DorianFGR")


print("Welcome to Rock Paper Scissors!")

game()

if input("Would you like to play again? (y/n)") == "y":

    game()

else:

    print("Thanks for playing!")
