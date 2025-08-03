shoppingList1 = ["Milk","Cheese","Butter","Tomato","Banana","Apple"]
shoppingList2 = ["Orange","Cheese","Kiwi","Tomato","Banana","Butter"] 

def listin(list1,list2):
    if list1 in list2: 
        print(list1,end=" ")

    
list(map(listin,shoppingList1,shoppingList2))

        
