# PPHA 30535: Python Programming for Public Policy
# Spring 2023
# HW2: Functions & Classes
# Author: Danya Sherbini

#############

# The following code generates a random password meeting the following criteria: 
## Includes uppercase and lowercase letters
## Special characters limited to: !@#$%^&*
## 8-16 characters in length
## Keyword argument named "special_chars" defaults to True
## If the function is called with the keyword argument set to False instead, then the random values chosen should
## not include special characters

import random
# from numpy import random

# creating the function
def pass_func(length, special = True, num = False): # adding in args and kwargs
    length = int(length) # making length an integer
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # defining letters
    numbers = '123456789' # defining numbers
    special_chars = '!@#$%^&*' # defining special characters
    while True:
        if length < 8 or length > 16: # if inputted length is less than 8 or more than 16
            print("Sorry, too short.") # print this
            break # and end the function
        if length >= 8 or length <= 16: # if the length is 8-16 then
            # apply these conditions depending on special and num arguments
            if special == True and num == False:
                alphabet = letters + special_chars
                # .join joins together the random symbols chosen with random.choice()
                password = ''.join(random.choice(alphabet) for i in range(length))
            elif special == True and num == True:
                alphabet = letters + special_chars + numbers
                password = ''.join(random.choice(alphabet) for i in range(length))
            elif special == False and num == True:
                alphabet = letters + numbers
                password = ''.join(random.choice(alphabet) for i in range(length))
            elif special == False and num == False:
                alphabet = letters
                password = ''.join(random.choice(alphabet) for i in range(length))
            return password


# testing out the function
pass_func(8) # with only the length argument + defaults
pass_func(8, True, True) # with letters + special chars + numbers
pass_func(12, False, True) # with only letters + numbers
pass_func(16, False, False) # with only letters