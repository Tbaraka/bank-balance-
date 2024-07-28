def credit_worthness(credit_limit, value):
    if value > credit_limit:
        print(f"The value of the goods is {value },Sorry you cannot purchase goods worthy such a value on credit")
    else:
        print(f"The value of the goods is {value },Thank you for purchasing from us")

n = int(input("Enter the number of customers: "))

for i in range(n):
    credit_limit = int(input(f"Customer {i+1}, enter your credit limit: "))
    while True:
        price = int(input("Enter the price of the item: "))
        quanity = int(input("Enter your quantity: "))
        value = price * quanity
        credit_worthness(credit_limit, value)
        if value > credit_limit:
            print("Please enter a lower value.")
        else:
            break
