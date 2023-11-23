import random
num2 = random.randint(1,99)
num1 = random.randint(1,99)
add = num1 + num2
subs = max(num1, num2) - min(num1, num2)
mult = num1 * num2
div = max(num1, num2) //min(num1, num2)
# Addition
ans=int(input(f'What is {num1}+{num2}?'))
if ans == add:
    print("Your answer is Correct!")
else:
    print("Your answer is Incorrect ")

# Subtraction
dif= int(input(f'What is {max(num1,num2)}-{min(num1,num2)}?'))
if dif == subs:
    print("Your answer is Correct ")
else:
    print("Your answer is Incorrect ")

# Multiplication
mult1 = int(input(f'What is {num1}x{num2}?'))
if mult1 == mult:
    print("Your answer is Correct ")
else:
    print("Your answer is Incorrect ")

# Division
div1 = float(input(f'What is {max(num1,num2)}/{min(num1,num2)}?'))
if div1 == div:
    print("Your answer is Correct ")
else:
    print("Your answer is Incorrect ")



