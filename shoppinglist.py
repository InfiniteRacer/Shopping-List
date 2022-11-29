def listitems():
    
    global yes
    global no
    
    yes = 'yes'
    no = 'no'
    
    print("Your items:")
    
    print("")
    
    print(list)
    
    print("")
    
    checkremove1=input("Do you need to remove any unwanted items? (yes/no) ")
    
    if checkremove1 == yes:
        
        print("")
        
        removew1=input("Enter the item name the EXACT SAME way you entered it: ")
        
        list.remove(removew1)
        
        checkremove2=input("Do you need to remove any more unwanted items? (yes/no) ")
        
        if checkremove2 == yes:
            
                print("")
                
                removew2=input("Enter the item name the EXACT SAME way you entered it: ")
        
                list.remove(removew2)
        
                checkremove3=input("Do you need to remove any more unwanted items? (yes/no) ")
                
                if checkremove3 == yes:
                    
                    print("")
                    
                    removew3=input("Enter the item name the EXACT SAME way you entered it: ")
        
                    list.remove(removew3)
        
                    checkremove4=input("Do you need to remove any more unwanted items? (yes/no) ")
                    
                    if checkremove4 == yes:
                        
                        print("")
                        
                        removew4=input("Enter the item name the EXACT SAME way you entered it: ")
        
                        list.remove(removew4)
        
                        checkremove5=input("Do you need to remove any more unwanted items? (yes/no) ")
                        
                        if checkremove5 == yes:
                            
                            print("")
                            
                            removew5=input("Enter the item name the EXACT SAME way you entered it: ")
                            
                            print("")
        
                            list.remove(removew5)
                            
                            print("You have reached the max amount of removes!")
                            
                            print("")
                            shopping()
                            
                        elif checkremove5 == no:
                            
                            print("")
                            shopping()
                        
                    elif checkremove4 == no:
                        
                        print("")
                        shopping()
                    
                elif checkremove3 == no:
                    
                    print("")
                    shopping()
            
        elif checkremove2 == no:
            
                print("")
                shopping()
        
    elif checkremove1 == no:
        print("")
        shopping()
        
def shopping():
    
    print("Lets get shopping!")
    
    print("")
    
    print("Here is your list:")
    
    print(list)
    
    print("")
    
    print("Instructions:")
    print("- The item you are getting is the item on the left of the list")
    print("For example, if the list was: ['Cheese', 'Milk', 'Butter',] The item you get is 'Cheese'.")
    print("Another example, if the list was: ['Milk', 'Cheese', 'Butter', 'Chocolate',] The item you get is 'Milk'.")
    
    checkpoint=input("Continue? (Enter anything) ")
    
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
            
        endpart()
        
    print("Next:")
    print("")
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
        
        endpart()
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
            
        endpart()
        
    print("Next:")
    print("")
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
        
        endpart()
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
            
        endpart()
        
    print("Next:")
    print("")
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
        
        endpart()
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
            
        endpart()
        
    print("Next:")
    print("")
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
        
        endpart()
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Next? (Enter anything) ")
            
    else:
            
        endpart()
        
    print("Next:")
    print("")
        
    if list:
            
        print(list)
        
        print("Next item is " +list.pop(0))
        
        print("")
        
        checkpoint=input("Finished? (Enter anything) ")
            
    else:
        
        endpart()
    
def endpart():
    
    print("")
    print("Shopping finished!")
    
    exit()

print("Shopping list: ")
print("")
print("Please note:")
print("")
print("Max 10 items in the list.")
print("You can only remove 5 in total items BEFORE you start shopping.")
print("")

global list

list = []

global yes
global no

yes = 'yes'
no = 'no'

item1=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item1)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()

item2=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item2)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()
    
item3=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item3)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()

item4=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item4)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()
    
item5=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item5)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()

item6=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item6)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()
    
list.append(item7)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()

item7=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item8)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()
    
item8=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item9)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()

item9=input("Item name: ")
print("")

check=input("Add another item? (yes/no) ")

list.append(item9)

if check == yes:
    print("")
elif check == no:
    print("")
    listitems()
    
item10=input("Item name: ")
print("")

print("Max items reached! ")
print("")

list.append(item10)

listitems()