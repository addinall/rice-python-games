# Mark Addinall
# vim: set expandtab tabstop=4 shiftwidth=4 autoindent:
# Interactive Python Programming
# Jan 2016 
# Rice University - Coursera MOOC
# Rock-paper-scissors-lizard-Spock
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#
# Build a helper function name_to_number(name) that converts the string name into a 
# number between 0 and 4 as described above. This function should use a sequence of 
# if/elif/else clauses. You can use conditions of the form name == 'paper', etc. to 
# distinguish the cases. To make debugging your code easier, we suggest including a 
# final else clause that catches cases when name does not match any of the five correct 
# input strings and prints an appropriate error message. 
#
# You can test your implementation of name_to_number() using this name_to_number testing 
# template. (Also available in the Code Clinic tips thread).
#
# Next, you should build a second helper function number_to_name(number) that converts 
# a number in the range 0 to 4 into its corresponding name as a string. Again, we suggest 
# including a final else clause that catches cases when number is not in the correct range. 
# You can test your implementation of number_to_name() using this number_to_name testing template.
#
# Implement the first part of the main function rpsls(player_choice). Print out a blank line 
#(to separate consecutive games) followed by a line with an appropriate message describing 
# the player's choice. Then compute the number player_number between 0 and 4 corresponding 
# to the player's choice by calling the helper function name_to_number() using player_choice.
#
# Implement the second part of rpsls() that generates the computer's guess and prints out 
# an appropriate message for that guess. In particular, compute a random number comp_number 
# between 0 and 4 that corresponds to the computer's guess using the function random.randrange(). 
# We suggest experimenting with randrange in a separate CodeSkulptor window before deciding on 
# how to call it to make sure that you do not accidently generate numbers in the wrong range. 
# Then compute the name comp_choice corresponding to the computer's number using the function 
# number_to_name() and print an appropriate message with the computer's choice to the console.
#
# Implement the last part of rpsls() that determines and prints out the winner. 
# Specifically, compute the difference between comp_number and player_number taken modulo five. 
# Then write an if/elif/else statement whose conditions test the various possible values of 
# this difference and then prints an appropriate message concerning the winner. 
# If you have trouble deriving the conditions for the clauses of this if/elif/else statement, 
# we suggest reviewing the "RPSLS" video which describes a simple test for determine the winner of RPSLS.

import random

random.seed()                                       # use the system time to seed the deterministic
                                                    # Mersenne Twister each time the program is executed

#------------------------
def name_to_number(name):
    ''' This function accepts a string as input
        Returns an integer RANK as output
        Returns -1 to indicate an error
    '''

    uname = name.lower()                            # cater for silly capitals - lowercase mix

    val = -1                                        # this will indicate an error in input

                                                    # convert name to number using if/elif
    if uname == 'rock':
        val = 0
    elif uname == 'spock':
        val = 1
    elif uname == 'paper':
        val = 2
    elif uname == 'lizard':
        val = 3
    elif uname == 'scissors':
        val = 4

    return val                                      # send it back


#--------------------------
def number_to_name(number):
    ''' This function accepts an integer as input
        This integer should be in the range 0..4
        We convert this RANK into a name and this becomes our output
        If the RANK is bad, we return ERROR as name
    '''
        
   
    name = 'error'                                  # default if the input is wonky
                                                    # convert number to a name using if/elif
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'

    return name                                     # send it back


#------------------------
def rpsls(player_choice): 
    '''  This in essence is the game
        Input - The item chosen by the 'player' as a string'
        Generates a random RANK for the computer to determine the item choice
        Converts this RANK to a string
        Informs the operator the player and the computer chosen items
        Evaluates the two RANKS on the 'Spock wheel'
        Informs the operator of the win/draw status of he outcome
        Output - None
    '''


    print                                           # print a blank line to separate consecutive games

    print 'Player chooses ' + player_choice         # print out the message for the player's choice

    player_number = name_to_number(player_choice)   # convert the player's choice to player_number using the 
                                                    # function name_to_number()
    if player_number == -1:
        print 'Player choice ' + player_choice + ' illegal. Bye.'    
                                                    # Bad choice of guess
        return                                      # Bug out
                                                    # otherwise ...
    comp_number = random.randrange(0,5)             # compute random guess for comp_number using random.randrange()
                                                    # [0 .. 4]

    comp_choice = number_to_name(comp_number)       # convert comp_number to comp_choice using the function number_to_name()
    if comp_choice == 'error':                      # should never happen, but...
        print 'Computer is Broken! NAME ERROR!'    
        return                                      # bug out
                                                    # otherwise ...
    print 'Computer chooses ' + comp_choice         # print out the message for computer's choice
                                            
    result = (player_number - comp_number) % 5      # compute difference of comp_number and player_number modulo five

                                                    # use if/elif/else to determine winner, print winner message
    if (result > 2):
        print 'Computer wins!'
    elif (result == 0):                             # this was not mentioned in the spec, but if the player and the
        print 'Player and computer tie!'            # computer both choose the same item, it's a draw!
    else:
        print 'Player wins!'


    
# do it Shelly!
 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# do it a few times to makes sure that the randomizer is randomizing

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# -----------------------------------------

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# -----------------------------------------

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# -----------------------------------------

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# end of five runs, although the player choice remained the same
# the computer choice differs, meeting the specification
# requirement for randomness

# test error condition

rpsls("muppet")

# ---------------------- EOF --------------------


