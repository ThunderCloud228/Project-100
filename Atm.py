class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def cashWithdrawl(self, amount):
        print("Successfully withdrew", amount, "cash")

    def cashDeposit(self, amount):
        print("Successfully deposited", amount, "cash")

    def balanceEnquiry(self):
        print("This is your bank balance")


Arush = Atm("007", "1010")

print(Arush)
print(Arush.cashWithdrawl("6969"))
print(Arush.cashDeposit("696969"))
print(Arush.balanceEnquiry())

