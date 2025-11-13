"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 1000000
while True: 
    Trumpcoin_AI = input("What shall you do with your money inferior Illegal Immigrant?")
    if Trumpcoin_AI == "withdraw":
        q = int(input(f"How much would you like to withdraw(and give to my inagural fund)?"))
        balance = (balance-q)
        print(f"You now have {balance}, Congratulations low iq person")
    elif Trumpcoin_AI == "check":
        print(f"you have {balance} in your account, soon I will give it and China 145% tariffs!")
    elif Trumpcoin_AI == "add":
        v = int(input("How much would you like to add Sleepy Joe?"))
        balance = v + balance 
        print(f"You now have {balance}, Congratulations low iq person")
    else:
        print("failure Government shutting down")