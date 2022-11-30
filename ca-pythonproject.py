#Project of int108
#Group 23
#project no- 23:
#ATM Functionality
#group members details:-
#Ayush Keshari, roll no-71 (12203620)
#Shivansh Raj, roll no-72 (12203621)
#Ashish Phogat, roll no-70(12215957)

print("Welcome to ABC Bank\n\nInsert your card")
print("Name: Mr.John")
choice=0
balance=10000
password=1234
pin=int(input("Enter your four digit pin:"))
if pin==password:
    while choice != 4:

        print("\n****Menu****\n")
        print("1 == Balance")
        print("2 == Deposit")
        print("3 == Withdraw")
        print("4 == Cancel\n")
        choice=int(input("Enter your option: "))

        if choice==1:
            print("Balance = ₹", balance)
            if balance < 5000:
                print("Low balance")

        elif choice==2:
            dep=int(input("Enter your  deposit amount: ₹"))
            balance += dep
            print("\nDeposited amount: ₹",dep)
            print("Balance: ₹",balance)
            if balance < 5000:
                print("Low balance")

        elif choice==3:
            wit = int(input("Enter the amount to withdraw: ₹"))
            balance -= wit
            print("\nWithdrawn amount: ₹",wit)
            print("Balance: ₹", balance)
            if balance < 5000:
                print("Low balance")


        elif choice==4:
            print("\nSession  ended! Thank you")

        else:
            print("Invalid entry!!")


else:
    print("Incorret pin! Try again")
