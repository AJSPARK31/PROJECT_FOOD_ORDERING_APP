import json
import random
import string




def AutoGenerate_FOOD_ID():
    '''Return a autogenerated random FooD ID'''
    Food_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    return Food_ID

        
def add_items(food_details_json,food_id,food_name,quantity,price,discount):
    food_details_dict={}
    food_details_dict["food_id"]=food_id
    food_details_dict["food_name"]=food_name
    food_details_dict["quantity"]=quantity
    food_details_dict["price"]=price
    food_details_dict["discount"]=discount
    f=open(food_details_json,"r+")
    content=json.load(f)
    content.append(food_details_dict)
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()
    return food_details_dict

def view_food_items(food_details_json):
    f=open(food_details_json,"r+")
    content=json.load(f)
    l=[]
    for i in content:
        l.append(i)
    return l


def edit_food_items(food_details_json):
    f=open(food_details_json,"r+")
    content=json.load(f)
    food_id=input("Enter food id : ")
    for i in range(len(content)):
        if  content[i]["food_id"]==food_id:
            user_input=int(input("Please enter from given options \n1. FOOD NAME \n2. Quantity \n3. Price \n4. Discount \n "))
            if user_input==1:
                new_details=input("Enter new detail : ")
                content[i]["food_name"]=new_details
                print(" Successfully Updated")
            elif user_input==2:
                new_details=input("Enter new detail : ")
                content[i]["quantity"]=new_details
                print(" Successfully Updated")
            elif user_input==3:
                new_details=int(input("Enter new detail : "))
                content[i]["price"]=new_details
                print(" Successfully Updated")
            elif user_input==4:
                new_details=int(input("Enter new detail : "))
                content[i]["discount"]=new_details
                print(" Successfully Updated")
            else:
                print("Enter correct option")
            
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            
    f.close()
    return 


def remove_food_items(food_details_json):
    f=open(food_details_json,"r+")
    content=json.load(f)
    food_id=input("Enter food id : ")
    for i in range(len(content)):
        if content[i]["food_id"]==food_id:
            del content[i]
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            print("Item Removed successfully")
    
    f.close()
    return True


def register(user_details_json):
    f=open(user_details_json,"r+")
    content=json.load(f)
    d={}
    user_name=input("Enter your name : ")
    user_phone=input("Enter your phone : ")
    user_address=input("Enter your address : ")
    user_email=input("Enter your Email : ")
    user_password=input("Enter your password :  ")
    d["user_name"]=user_name
    d["user_phone"]=user_phone
    d["user_address"]=user_address
    d["user_email"]=user_email
    d["user_password"]=user_password
    content.append(d)
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()
    return 


def user_log_in(user_details_json):
    f=open(user_details_json,"r+")
    content=json.load(f)
    user_phone=input("Enter your phone : ")
    user_password=input("Enter your password : ")
    
    for i in range(len(content)):
        if content[i]["user_phone"]==user_phone and content[i]["user_password"]==user_password:
            print("log in successfully")
            

def place_new_order(food_details_json):
    f=open(food_details_json,"r+")
    content=json.load(f)
    
    for i in range(len(content)):
        l=[]
        food_name=content[i]["food_name"]
        quantity=(content[i]["quantity"],)
        price=["INR "+str(content[i]["price"])]
        l.append(food_name)
        l.append(quantity)
        l.append(price)
        print(str(i+1)+".",l)
    food_order_input=input("\nEnter your order  ").split(",")
    f=open("food_details","r+")
    content=json.load(f)
    for i in range(len(content)):
        l2=[]
        for j in range(len(food_order_input)):
            if i+1==int(food_order_input[j]):
                ordered_food_name=content[i]["food_name"]
                ordered_quantity=(content[i]["quantity"],)
                ordered_price=["INR "+str(content[i]["price"])]
                l2.append(ordered_food_name)
                l2.append(ordered_quantity)
                l2.append(ordered_price)
                print(l2)
                user_confirmation=int(input("\nPlace your order\n1. Yes\n2. No\n"))
                if user_confirmation==1:
                    user_confirmation=int(input("Confirm if you want to save your order into history section\n1. Yes\n2. No"))
                    if user_confirmation ==1:
                        f_user_details=open("user_details","r+")
                        content_user_details=json.load(f_user_details)
                        user_phone=input("Please enter your phone : ")
                        for i in range(len(content_user_details)):
                            if content_user_details[i]["user_phone"]==user_phone:
                                content_user_details[i]["order_history"].append(l2)
                                f_user_details.seek(0)
                                f_user_details.truncate()
                                json.dump(content_user_details,f_user_details)
                                f.close()
                            
                        print("Your order is Placed and saved into order history")
                    
        
                    else:
                        print("Your order is Placed")
                        
                        print("You Chooses not to save in order history")
                        
                    
                    
                else:
                       print("You Cancelled your order")
                    
    
    f.close()
    return
def update_profile(user_details_json):
    f=open(user_details_json,"r+")
    content=json.load(f)
    user_phone=input("Enter your phone")
    for i in range(len(content)):
        if content[i]["user_phone"]==user_phone:
            user_input_for_updation=int(input("Enter options from given below : \n1. Name\n2. Address\n3. Email\n4. Password\n"))
            if user_input_for_updation==1:
                new_detail=input("Enter your new name : ")
                content[i]["user_name"]=new_detail
                print("Updated Successfully")
            elif user_input_for_updation==2:
                new_detail=input("Enter your new address : ")
                content[i]["user_address"]=new_detail
                print("Updated Successfully")
            elif user_input_for_updation==3:
                new_detail=input("Enter your new email : ")
                content[i]["user_email"]=new_detail
                print("Updated Successfully")
            elif user_input_for_updation==4:
                new_detail=input("Enter your new password : ")
                content[i]["user_password"]=new_detail
                print("Updated Successfully")
            else:
                print("Choose correct options")
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
    f.close()
    return

def order_history(user_details_json):
    f=open(user_details_json,"r+")
    content=json.load(f)
    user_phone=input("Enter your phone :")
    for i in range(len(content)):
        if content[i]["user_phone"]==user_phone:
            order_history=content[i]["order_history"]
            if len(order_history)==0:
                print("There is no order to show")
                break
            else:
                for i in range(len(order_history)):
                    print("Order "+ str(i+1) ,order_history[i])
                break
    else:
        print("Enter correct phone no")
        
    f.close()
    return
       
       