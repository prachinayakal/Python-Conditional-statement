#Conditional Statement in Python
# if statement 
# if the condition in if is true it will print the statement 
# if the condition is not true it will not print anything
a = 25
if (a>10):
    print("a is greater than 10.") #if statement
    

#if-else statement
# if the condition if is true it will print the statement in if part
# if the condition in if is not true it will print the else statement
a = 25
if (a>30):
    print("a is greater than 30.") # if statement
else:
    print("a is less than 30.") # else statement


# elif statement
# this statement consist of multiple if-else conditions
# if the condition if is true it will print the if statement
# if the condition in if is not true it will check the condition for elif if the condition in elif is true it will print the statement
# if the elif condition is not true then it will print else part

a = 75
if (a==10):
    print("a is equal to 10.")
elif (a<50):
    print("a is less than 50.")
else:
    print("a is neither equal to 10 nor less than 50.")