"""
Erick Gonzalez Cruz
Started: 7/2/2025
File: A simple calculator!
"""


#Well first of all think of what a calculator needs! 
"""
Think of wether or not its more usefull to put in inheritance to get everything together!
Also think of ways of how I am able the amount of classes! 
DONT USE ANY AI Please.
Learn how to search better on google
"""
class User:
    def __init__(self, user):
        self.user = user
    
    def action_1(self):
        num_str = input("Enter your First number: ")
        num_int = int(num_str)
        return num_int
    
    def action_2(self):
        num_str = input("Enter your Second number: ")
        num_int = int(num_str)
        return num_int
    
#Figure out how to inherint from use to get both number and put it into my calcultor class
class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def addition(self, num_1, num_2):
        return num_1 + num_2

    def subtraction(self, num_1, num_2):
        return num_1 - num_2

    def multiplication(self, num_1, num_2):
        return num_1 * num_2

    def division(self, num_1, num_2):
        return num_1 // num_2
    
"""
To get this shi work:
1. I need to make action for first and second number (Seperate!), 
Like ask first number then the second 
2. Ask the user the type of action they want to do!!!
"""

if __name__ == "__main__":
    Calc = Calculator(1, 2)
    Player = User("Player")

    print("This is a basic calculator app")
    print("-" * 75)

    num_1 = Player.action_1()
    num_2 = Player.action_2()

    # Calc.addition(num_1, num_2)
    print(Calc.addition(num_1, num_2))
    


"""
Enter your first number: ___
Enter your second number: ___
What type of action do you want to do? _(+, -, *, //)___
Here is the result: _result_
"""