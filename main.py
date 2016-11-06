import csv
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
    print("Items added to the inventory")
    print_table("count,desc")

def print_table(order="default"):
    if order in ["count,asc", "count,desc", "default", "asc", "desc", " "]:
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

        if order in [" ", "default"]:
            inv_print = inv
        if order in ["asc", "count,asc"]:
            inv_print = OrderedDict(sorted(inv.items(), key=lambda t: t[1]))
        if order in ["desc", "count,desc"]:
            inv_print = OrderedDict(sorted(inv.items(), key=lambda t: t[1], reverse=True))

        for key, value in inv_print.items():
            print(str(value).rjust(valueLength), key.rjust(keyLength))
        print("-"*(valueLength+keyLength+1))
        print("Total number of items: ", total_value)
    else:
        print("Please use the: asc, desc or leave it blank.")


def import_inventory(filename="import_inventory.csv"):
    try:
        file = open(filename, "r")
        read = csv.reader(file, quoting=csv.QUOTE_MINIMAL, doublequote=False)
        next(read)
        impinv = dict((row[0], int(row[1]))for row in read)
        file.close()
        for key, value in impinv.items():
            if key in inv:
                inv[key] += value
            else:
                inv[key] = value
        print("Succesfully imported! The updated invetory looks like this:\n")
        print_table("count,desc")
    except FileNotFoundError:
        print("The given file does'nt exist.")

def export_inventory(filename="export_inventory.csv"):
    firstrow = open(filename, "w")
    firstrow.write("item_name,count\n")
    firstrow.close()
    file = open(filename, "a")
    writer = csv.writer(open(filename, 'a'))
    writer.writerows(inv.items())
    file.close()

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
impinv = {}

print("Hello dear!")

while True:
    answer = input("\n   Press \nD for display inventory\nL to pick up the dragon loot\nP to print the inventory, well organized\nI for import and megre an inventory\nE for export the inventory\n").upper()
    if answer == "D":
        display_inventory()
    elif answer == "L":
        add_to_inventory(inv, dragon_loot)
    elif answer == "P":
        ordering = input("Choose an ordering type:\n desc - for descending\n asc - for ascending\n or leave it blank for a random order\n")
        if len(ordering) > 1:
            print_table(ordering)
        else:
            print_table()
    elif answer == "I":
        filename = input("Add the name of the file or leave it blank for importing from import_inventory.csv\n")
        if len(filename) > 1:
            import_inventory(filename)
        else:
            import_inventory()
    elif answer == "E":
        filename = input("Add the name of the exported file or leave it blank to be called export_inventory.csv\n")
        if len(filename) > 1:
            export_inventory()(filename)
        else:
            export_inventory()()