print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?"))
tip_percentage= input("How much tip would you like to give? 10, 12, or 15?")
tip= int(tip_percentage)*(bill)/100
split=int(input("How many people to split the bill?"))
print(f"Each person should pay: ${(bill+tip)/split:.2f}")
