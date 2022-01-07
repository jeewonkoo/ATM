class Bank:
    def __init__(self, PIN, balance = 0):
        self.PIN = PIN
        self.balance = balance

    def insertCard():
        print("Please Insert card to begin transaction.")
        card = input("(Type 'card' for simplification) : ")
        if card != "card": 
            print("Invalid card. Transaction failed.") 
            return False
        else: 
            print("Successfully read card.")
            return True
        

    def readPIN():
        pinNum = input("Please enter your PIN number: ")
        return pinNum
    
    def getPIN(self):
        return self.PIN

    def selectAccount():
        print("Select account you want to make transaction.")
        account = input("1. Checking / 2. Saving: ")
        return account 


    def checkBalance(self):
        return self.balance

    def deposit(self):
        print("Your current balance is $" + str(self.balance))
        deposit_amount = input("Enter amount of money you want to deposit: ")
        if int(deposit_amount) < 1: 
            print("Invalid deposit amount. Transaction cancelled.")
            print("Please start from beginning.")
            return
        self.balance += int(deposit_amount)
        print("$" + str(deposit_amount) + " will be added to yout account.")
        print("Total balance: $" + str(self.balance))
        print("Transaction finished.")
        #Reciept 

    def withdraw(self):
        print("Your current balance is $" + str(self.balance))
        withdraw_amount = input("Enter amount of money you want to withdraw: ")
        if int(withdraw_amount) > self.balance:
            print("You can't withdraw more than your current balance. Transaction cancalled.")
            print("Please start from beginning.")
            return
        self.balance -= int(withdraw_amount) 
        print("$" + withdraw_amount  + " will be withdrawn from yout account.")
        print("Total balance: $" + str(self.balance))


