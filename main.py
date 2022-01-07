
from Bank import * 
import random

print("Welcome to JK Bank.")
print("Do you want to make a new transaction?")
answer = input("Please Enter Y / N: ")
print("")
if answer == "Y" : transaction = True
else: transaction = False

while transaction: 
    readCard = Bank.insertCard()
    if not readCard:
        break
    
    b1 = Bank(hash(9999), random.randint(1,10000))

    print("")
    pinNum = Bank.readPIN()
    
    if b1.getPIN() == hash(int(pinNum)): print("PIN number matches.")
    elif b1.getPIN() != pinNum : 
        print("Invalid PIN number. Transaction failed.")
        break

    print("")

    account = Bank.selectAccount()
    if account == "1" :
        print("Checking account is selected.")
    elif account == "2": 
        print("Saving account is selected.")
    else: 
        print("Invalid selection. Transaction failed.")
        break

    print("")
    print("Choose number of what you want to do")

    task = input("1. Check balance / 2. Deposit / 3. Withdraw : ")

    if task == "1": 
        balance = b1.checkBalance()
        print("Your current balance is " + "$" + str(balance))
    elif task == "2" : b1.deposit()
    elif task == "3" : b1.withdraw()
    else: 
        print("Invalid selection. Transaction failed.")
        break

    print("Do you want to make another transaction?")
    ans = input("Y / N : ")
    if ans == "N": break

print("Thank you for using JK Bank.")