class Atm(object):
    def __init__(self):
        cardNumber = int(input("Enter your card number here: "))
        pinNumber = int(input("Enter your pin number here: "))

    def cashWithdrawl(self):
        amount = int(input("Enter the amount of cash you want to withdraw: "))
        print("Successfully withdrew", amount, "cash")

    def cashDeposit(self):
        amount1 = int(input("Enter the amount of cash you want to deposit: "))
        print("Successfully deposited", amount1, "cash")

    def balanceEnquiry(self):
        print("This is your bank balance")


Arush = Atm()

print(Arush)
print(Arush.cashWithdrawl())
print(Arush.cashDeposit())
print(Arush.balanceEnquiry())

