# print("hello world")
# #print is a function that prints out a message on the console
# #strings are surrounded by quotes
# #single or double ' ' or ""
# # whenever a word is surrounded by quotes it is called a string 
# #be consistent with the quote you use 
# print("Lucas Valles")
# print("order of exuction")
# print("in pyhton")
# print("*"*20)
# #variables are used to store data
# #variables are created when you assign a value to it 
# #variables are case sensitive 
# price = 10 #integer variable 
# name = "john" #srting variable
# rating = 4.9 #float variable
# is_published = True #boolean variable
# #start all variables with a lower case letter or underscore
# print("name")
# print("Price")
# print("rating")
# #string interpolation when you can use variables in a sentence
# print(name + " is a basketball player ")
# # concatemation to join variables in a sentence using 
# # the plus (+) sign
# print(name + " has a rating of " + str(rating))
# #use the str() function to convert a number to a string 
# # this is called type conversion
# print("the orice of the is " + str(price))
# # # getting input from the user


name = input("Enter your name:")
while name == "":
    print("You did not enter your name")
    name= input("enter your name")

    age = int(input("Enter your age:"))
    while age < 0:
        print(f"you are (age) years old")

        food = input("enter a food you like")

        while food == "q":
            print(f"You like (food)")
            food = input ("enter your name")

            num = input("enter a number between 1 - 10")
            while our (num)< 1 or num > 10:
print(f"(num)"is not valid)
print("your number is (num)")
#wildloops