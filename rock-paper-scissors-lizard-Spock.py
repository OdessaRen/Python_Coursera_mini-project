# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

#input code:
#guess = str(input('please enter your choice'))   

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if (name == 'rock'):
        number=0
    elif (name == 'Spock'):
            number = 1
    elif (name == 'paper'):
        number= 2
    elif (name == 'lizard'):
        number = 3
    elif (name == 'scissors'):
        number = 4
    else:
        print 'name invalid!'
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
      if (number == 0):
        name = 'rock'
      elif (number == 1):
            name = 'Spock'
      elif (number == 2):
        name = 'paper'
      elif (number == 3):
        name = 'lizard'
      elif (number == 4):
        name = 'scissors'
      else:
        name = 'invalid!'
  
      return name

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    import random
    c_choice = random.randrange(0,4)
    p_choice = name_to_number(player_choice)
    
    computer_choice = number_to_name(c_choice)
    print "player chooses:"+player_choice
    print "computer chooses:"+computer_choice
    if (c_choice==p_choice):
        result = 'tie'
    elif(c_choice+2<5):
        if(c_choice-p_choice==-1 or c_choice-p_choice==-2):
            result = 'you win!'
        else:
            result = 'computer wins!'
    elif(c_choice+2>4):
        if(c_choice-p_choice==1 or c_choice-p_choice==2):
            result = 'computer wins!'
        else:
            result = 'you win!'
    else: 
        result = 'input not correct!'
    
    print result
    print ""
    
    
      
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
#guess = str(input('please enter your choice'))   
#rpsls(guess)

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

