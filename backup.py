import collections
from collections import OrderedDict


def display_inventory():
    print("Inventory: ")
    for i in inv:
        print(inv[i], i)

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    display_inventory()

def print_table(order="default"):
    print(order)
    if order in ["count,asc", "count,desc", "default"]:
        valueLength, keyLength = 0,0
        total_value = 0
        inv_print = {}
        for k, v in inv.items():
            total_value = total_value + v
            if valueLength < len(str(v)):
                valueLength = len(str(v))
            if keyLength < len(str(k)):
                keyLength = len(str(k))
        valueLength, keyLength = valueLength+4, keyLength+4
        print("Count".rjust(valueLength), "Item name".rjust(keyLength))
        print("-"*(valueLength+keyLength+1))
        if order == "default":
            inv_print = inv
        if order == "count,asc":
            inv_print = OrderedDict(sorted(inv.items(), key=lambda t: t[1]))
        if order == "count,desc":
            inv_print = OrderedDict(sorted(inv.items(), key=lambda t: t[1], reverse=True))

        for key, value in inv_print.items():
            print(str(value).rjust(valueLength), key.rjust(keyLength))
        print("-"*(valueLength+keyLength+1))
        print("Total number of items: ", total_value)
    else:
        print("Please use the: count,asc or the count,desc.")
        
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#add_to_inventory(inv, dragon_loot)
#print_table('i')


print_table()
