print("Welcome to the tip calculator.")
billTotal = float(input("\nWhat is your total bill ? $"))
tip = int(input("How much tip would you like to give? 10, 12 0r 15? "))
splitBill = int(input("How many people are you splitting bills with: " ))
billTip = (tip / 100 + 1) * billTotal
billPerPerson = billTip /splitBill
billTotal = "{:.2f}".format(billPerPerson)
print(f"\nEach person should pay ${billTotal} $" )
