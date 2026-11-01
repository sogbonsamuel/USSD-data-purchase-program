#Assignment... 

#Create a realistic USSD for buying data with any network of your choice. Glo, MTN, Airtel etc

#From where you type *312# up until where you have "You have successfully purchased ##MB of data"

import time


balance = 1000
data = 0

code = input("Dial: ")

if code == "*312#":
    print("USSD code running....")
    time.sleep(2.0)
elif code != "*312#":
    print("Invalid USSD code")
    exit()

print("\nMTN Data Plans")
print("1. 100MB - N100")
print("2. 500MB - N300")
print("3. 1GB - N500")

choice = (int(input("Reply: ")))
data = 0
price = 0

if choice == 1:
    data = 100
    price = 100
elif choice == 2:
    data = 500
    price = 300
elif choice == 3:
    data = 1024
    price = 500
else:
    print("Invalid choice")

for choice in range(1, 4):
    if choice == 1 and balance >= price:
        balance -= price
        print(f"You have successfully purchased {data}MB of data. Your new balance is N{balance}.")
        break
    elif choice == 2 and balance >= price:
        balance -= price
        print(f"You have successfully purchased {data}MB of data. Your new balance is N{balance}.")
        break
    elif choice == 3 and balance >= price:
        balance -= price
        print(f"You have successfully purchased {data}MB of data. Your new balance is N{balance}.")
        break
    else:
        print("Insufficient balance or invalid choice.")
