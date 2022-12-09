item1=input("Enter Item 1")
item2=input("Enter item 2")
Grocery_items=["Egg","Bread","Apple","Milk","Flour"]
if item1 in Grocery_items and item2 in Grocery_items:
    print("Both items are in Grocery")
elif item1 in Grocery_items and item2 not in Grocery_items:
    print(item1,"is in Grocery but",item2,"is not in grocery")
elif item2 in Grocery_items and item1 not in Grocery_items:
    print(item2,"is in Grocery but",item1,"is not in grocery")
else:
    print("Both items are not in Grocery")