
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

def print_table(order):
    if order == '':
        pass
    if order in ['igen']:
        print("farok")
    '''if order == 'nem', 'ne', 'n':
        print("pina")'''
        
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#add_to_inventory(inv, dragon_loot)
#print_table('i')
valueLength, keyLength = 0,0
for k, v in inv.items():
    if valueLength < len(str(v)):
        valueLength = len(str(v))
    if keyLength < len(str(k)):
        keyLength = len(str(k))
print(valueLength, keyLength)
valueLength, keyLength = valueLength+4, keyLength+4
print(valueLength, keyLength)
print("count".rjust(valueLength), "item name".rjust(keyLength))
print("-"*(valueLength+keyLength+1))
for key, value in inv.items():
    print(str(value).rjust(valueLength), key.rjust(keyLength))


