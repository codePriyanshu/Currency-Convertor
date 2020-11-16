with open("Currency-Data.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter Amount To Convert Into - "))
print("Enter The Name Of Currency You Want To Convert Into. Available Currencies Are - ")
[print(item) for item in currencyDict.keys()]
currency = input("Please Enter The Currency Name - ")
print(f"{amount} INR Is Equals To {amount * float(currencyDict[currency])} {currency}")