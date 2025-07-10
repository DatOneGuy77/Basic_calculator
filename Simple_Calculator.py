"""
Erick Gonzalez Cruz
Started: 7/2/2025
File: A simple calculator!
Completed: 7/9/2025
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
    

if __name__ == "__main__":
    Calc = Calculator(1, 2)
    Player = User("Player")

    print("This is a basic calculator app")
    print("-" * 75)

    #store the value of the number that was asked in class User
    num_1 = Player.action_1()
    num_2 = Player.action_2()

    #Making sure user only puts the options I gave them
    print("Options are: +, -, //, *")
    chose_operation = input("What type of arithmetic operation would you like: ")

    #Storing each individual operation in seperate outcome
    if chose_operation == "+":
        sum_result = Calc.addition(num_1, num_2)
        print(f"The result is: {sum_result}")
    elif chose_operation == "-":
        subtract_result = Calc.subtraction(num_1, num_2)
        print(f"The result is: {subtract_result}")
    elif chose_operation == "//":
        divide_result = Calc.division(num_1, num_2)
        print(f"The result is: {divide_result}")
    elif chose_operation == "*":
        multiplied_result = Calc.multiplication(num_1, num_2)
        print(f"The result is: {multiplied_result}")

