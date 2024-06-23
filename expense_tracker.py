import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

expenses = []
exp_1 = {'amount': '399', 'category': 'Book: Atmoic habit'}
expenses.append(exp_1)
exp_2 = {'amount': '100.25', 'category': 'medicines'}
expenses.append(exp_2)

def removeExpense():
    while True:
        listExpenses()
        print(Fore.MAGENTA + f"   What expense would you like to remove?")
        try:
            expenseToRemove = int(input(Style.BRIGHT + f" ->"))
            del expenses[expenseToRemove]
            break
        except:
            print(Fore.RED + f"   Invaild input. Please try again.")
            print()

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)


def printMenu():
    print(Style.BRIGHT + f"\U000025FEPlease choose from one of the following options...")
    print("   1. Add a new Expense")
    print("   2. Remove an Expense")
    print("   3. List all Expense")
    print("   4. Press 'q' to quit")

def listExpenses():
    print(Fore.LIGHTBLUE_EX + f"   Here is a list of your expenses....")
    print(Fore.BLUE + Style.BRIGHT +  f"   -------------------------------------")
    counter = 0
    for expense in expenses:
        print(f"   # {counter} - {expense['amount']} - {expense['category']}")
        counter += 1
    print()


if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input(Style.BRIGHT + f" ->")
        print()

        if optionSelected == '1':
            print(Fore.MAGENTA + f"   How much was this expense? ")
            while True:
                try:
                    amountToAdd = input(Style.BRIGHT + f" ->")
                    break
                except:
                    print(Fore.RED + f"   Invaild input. Please try again.")

            print(Fore.MAGENTA + f"   What category was this expense? ")

            while True:
                try:
                    category = input(Style.BRIGHT + f" ->")
                    print()
                    break
                except:
                    print(Fore.RED + f"   Invaild input. Please try again.")

            addExpense(amountToAdd,category)

        elif optionSelected == '2':
            removeExpense()
        elif optionSelected == '3':
            listExpenses()
        elif optionSelected == 'q':
            print("Have a Great Day.")
            break
        else:
            print(Fore.RED + f"   Invaild input. Please try again.")