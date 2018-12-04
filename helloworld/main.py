def add(num1, num2):
    """Returns num1 plus num2. """
    return num1 + num2

def sub(num1, num2):
    """Returns num1 minus num2. """
    return num1 - num2

def mul(num1, num2):
    """Returns num1 multiplied by num2. """
    return num1 * num2

def div(num1, num2):
    """Returns num1 divided by num2. """
    return num1 / num2\

def main():
    """Allows user to run basic calculator operations with two numbers."""
    user_continue = True
    while user_continue:
        validInput = False
        while not validInput:
            #  until valid input, try to get valid input.
            try:
                num1 = int(input("First Number?")
                           )
                num2 = int(input("Second Number?")
                           )
                operation = int(input("What do you want to do? 1)add 2)subtract 3)multiply 4)divide "))
                validInput = True
            except:
                print("invalid input, try again.")

        if(operation == 1):
            print("Adding...")
            print(add(num1, num2))

        elif(operation == 2):
            print("Subtracting...")
            print(sub(num1, num2))

        elif(operation == 3):
            print("Multiplying...")
            print(mul(num1, num2))

        elif(operation == 4):
            print("Dividing...")
            print(div(num1, num2))

        else:
            print("I don't understand.")
        # Ask user to continue
        user_yn = input('Would you like to run another calculation? ("y" for yes or any other value to exit)')
        if(user_yn != 'y'):
            user_continue = False
            break
        else:
            continue


main()
