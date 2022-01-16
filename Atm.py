class Atm(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardNumber = cardnumber
        self.pinNumber = pinnumber

    def BalanceEnquiry(self):
        print("Your balance is 10,000")

    def CashWithdrawl(self, amount):
        newAmount = 100000 - amount
        print("You have withdrawn amount "+ str(amount) + '. ' + "Your remaining amount is "+ str(newAmount))


cardNumber = int(input("Enter your card number : "))
pinNumber  = int(input("Enter your pin number : "))

newUser = Atm(cardNumber, pinNumber)

print(newUser.BalanceEnquiry())
amount = int(input("Enter the amount you would like to withdraw: "))
print(newUser.CashWithdrawl(amount))
