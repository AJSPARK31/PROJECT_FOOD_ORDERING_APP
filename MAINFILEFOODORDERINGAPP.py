#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
from json import JSONDecodeError
import foodcode


while True:
    user_input=int(input("WELCOME TO AJ RESTURANT\n1. Admin \n2. User\n3. Exit\n"))
    if user_input==1:
        username=input("Enter your user name \n")
        password=input("Enter your password \n")
        f=open("admin_details","r+")
        content=json.load(f)
        for i in range(len(content)):
            if username in content[i]["User Name"]==username and content[i]["Password"]==password:
                print("\nLogin successfully")
                admin_input=int(input("Enter your action\n1. ADD FOOD ITEMS\n2. STOCK\n3. EDIT FOOD ITEMS \n4. VIEW FOOD ITEMS \n5. REMOVE FOOD ITEMS \n6. EXIT\n"))
                if admin_input==1:
                    food_id=foodcode.AutoGenerate_FOOD_ID()
                    food_name=input("Enter Food Name : ")
                    quantity=input("Enter Quantity : ")
                    price=int(input("Enter Price of food in Rs : "))
                    discount=int(input("Enter the discount in percentage : "))
                    adding_items=foodcode.add_items("food_details",food_id,food_name,quantity,price,discount)
                elif  admin_input==2:
                    pass
                elif admin_input==3:
                    edit_food_item= foodcode.edit_food_items("food_details")
                elif admin_input==4:
                    view_food_items=foodcode.view_food_items("food_details")
                    print(view_food_items)
                elif admin_input==5:
                    remove_food_items=foodcode.remove_food_items('food_details')
                elif admin_input==6:
                    break
                else:
                    print("CHOOSE CORRECT OPTIONS")
            
            
            
            
            else:
                print("\nIncorrect username or password")
                
    elif user_input==2:
        user_in=int(input("Enter your choice \n1. Register \n2. log in \n"))
        if  user_in==1 :
            user_registration=foodcode.register("user_details")
            print('Registration Successfully')
            
        elif user_in==2:
            user_login=foodcode.user_log_in("user_details")
            user_input=int(input("Enter option from given below : \n1. PLACE NEW ORDER\n2. ORDER HISTORY\n3. UPDATE PROFILE\n4. EXIT\n"))
            if user_input==1:
                place_new_order=foodcode.place_new_order("food_details")
                
                
            elif user_input==2:
                order_history=foodcode.order_history("user_details")
            elif user_input==3:
                user_profile_updation=foodcode.update_profile("user_details")
            elif user_input==4:
                break
                           
            else:
                print("Choose Correct option")
        else:
            
            print("Enter correct option ")
            break
    elif user_input==3:
        break
    else:
        print("Choose Correct Options")


# In[ ]:




