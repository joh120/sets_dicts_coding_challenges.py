# Challenge 1 - Sum up all the items in a dictionary


fruits = {'apples':10, 'bananas':12, 'oranges':15}

count = 0 

for key, value in fruits.items():
    count = count + value 

sumOfFruits = count 

print(f"We have a total of {sumOfFruits} pieces of fruit")

print("------------------------------------")

# Challenge 2 - Inventory Management system 
#               Users can add, update or remove items from inventory


shoe_stall = {"name": "timbaland boots", 
              "price": 120, 
              "quantity": 30}

def addItem(newKey, newValue):

    shoe_stall[newKey] = newValue


def removeItem(removeItem):
    del shoe_stall[removeItem]

def updateItem(a,b):
    shoe_stall.update({a:b})

addItem(10,20)
removeItem("price")
updateItem("quantity", 80)

print(shoe_stall)


print("------------------------------------")


# Challenge 3- Keys are departments in a company
#              Values are dictionaries 
#              containing employee information (name, role)


notSonyltd = {
              "IT":{"employee": "Jim", "role": "developer"},
              "Accounting":{"employee": "Carter", "role": "accountant"},
              "Management":{"employee": "Jill", "role": "CEO"},
              "Admin":{"employee": "April", "role": "admin"}
              }

print(notSonyltd["IT"])

print("------------------------------------")


# Challenge 4- Write a function to create a new set that contains 
#              the identical items from two given sets.


def onlyDuplicates(a,b):
    
    newSet = a.intersection(b)

    return newSet

print(onlyDuplicates({1, 2, 3, 4}, {3, 4, 5, 6}))
