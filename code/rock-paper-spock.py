# Mark Addinall
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

#------------------------
def name_to_number(name):
    # delete the following pass statement and fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!



#--------------------------
def number_to_name(number):
    # delete the following pass statement and fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    


#------------------------
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# do it Shelly!
 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# EOF

