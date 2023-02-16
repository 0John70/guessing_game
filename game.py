#This program demonstrates a guessing game
from random import randint
#get user input
user_name = input("Please enter your name: ")
print("Hello there " + user_name + "!")
#generate the random number
random_number = randint(10, 50)
counter = 0

#Using a while loop
while counter <5:
    user_number = eval(input("Please input your number: "))
    counter +=1

# check if user input is equal to generated number
    if user_number< random_number:
      print("Your guess is too low.")
    elif user_number>random_number:
     print("Your guess is too high.")
    elif user_number ==random_number:
       break 
if user_number == random_number:
    print("You win!")
else:
    print("Game over. The correct number is: ")
    print(random_number)    
   



