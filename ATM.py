class ATM(object):
    def __init__(self, pin, cardnum, balance):
        self.pin = pin
        self.cardnum = cardnum
        self.balance = balance
    
    def cashwithdrawal(self):
        amount = int(input("How much money would you like to withdraw? "))
        print("Withdrawing money...")
        b = self.balance - amount
        self.balance = str(b)
        print("Withdrawal successful. Your balance:" ,self.balance)

    def cashdeposit(self):
        amount = int(input("How much money would you like to deposit? "))
        print("Depositing money...")
        b = self.balance + amount
        self.balance = str(b)
        print("Deposit successful. Your balance:" ,self.balance)

    def balanceenquire(self):
        print("Checking amount of balance...")
        print("Check successful. Your balance:" ,self.balance)


def main():
    print("Bank of Byju's Future School ATM")
    print("First of all, let's create your account.")
    piin = input("What is your credit/debit card PIN going to be? ")
    num = input("What is your credit/debit card number going to be? ")
    balan = int(input("What is your principal deposit amount going to be? "))
    me = ATM(piin, num, balan)
    print("Type WITHDRAW to withdraw cash from your bank account.")
    print("Type DEPOSIT to deposit cash into your bank account.")
    print("Type ENQUIRY to check your bank account balance.")
    print("Type EXIT to exit.")
    com = input("What would you like to do? ")
    if (com == "WITHDRAW"):
        me.cashwithdrawal()
    elif (com == "DEPOSIT"):
        me.cashdeposit()
    elif (com == "ENQUIRY"):
        me.balanceenquire()
    else:
        print("That command does not exist. Please try again.")

main()