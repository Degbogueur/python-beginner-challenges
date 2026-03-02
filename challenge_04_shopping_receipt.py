item_01_name = input("Enter item 1 name: ")
item_01_price = float(input("Enter item 1 price: "))
item_02_name = input("Enter item 2 name: ")
item_02_price = float(input("Enter item 2 price: "))
item_03_name = input("Enter item 3 name: ")
item_03_price = float(input("Enter item 3 price: "))

total = item_01_price + item_02_price + item_03_price

print("\n---------------------")
print(f"{item_01_name}\t\t${item_01_price:.2f}")
print(f"{item_02_name}\t\t${item_02_price:.2f}")
print(f"{item_03_name}\t\t${item_03_price:.2f}")
print("---------------------")
print(f"TOTAL\t\t${total:.2f}")