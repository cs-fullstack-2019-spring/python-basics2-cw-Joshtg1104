import random


def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()



# ### Problem 1:
# Create a random number. Print the number.
#
# ```
# Hint:
# import random
# randomNumber = random.randint(0,9)
# ```

def problem1():
    randomNum = random.randint(0,28)
    print(randomNum)


# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.

def problem2():
    entry = input("Enter a string")

    while True:
        if(entry == "q"):
            break
        else:
            entry = input("Enter another string")
            continue

# ### Problem 3:
# Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'.
# Repeat.

def problem3():


    while True:
        enterNum = int(input("Enter a positive number"))
        if(enterNum == 0):
            break
        else:
            for num in range(enterNum+1):
                print(num)
            continue


# ### Problem 4:
# Create a function that creates a random number.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.

def problem4():
    randomNum = random.randint(0,9)

    while True:
        entry = int(input("Guess the magic number"))
        if(entry == randomNum):
            break
        elif(entry > randomNum):
            print("Go Lower")
            continue
        elif(entry < randomNum):
            print("Go Higher")
            continue




if __name__ == '__main__':
    main()