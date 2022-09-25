#!/usr/bin/env python
# coding: utf-8

# In[30]:


# user panel
import os
import pickle

user = str(input("enter your operation: "))
Name = input("Enter your name: ")
Phone_Number = int(input("Enter your moblie number: "))
Email = str(input("Enter your email_id: "))
Password = str(input("Enter your password: "))
Address = str(input("Enter your address: "))
    



# In[31]:


class login:
    def __init__(self,id,pas):
        self.id = id
        self.pas = pas
        
    def check(self, id, pas):
        
        if self.id == id and self.pas == pas:
              return self.id,self.pas
            
log = login(" "," ")
log.check(input("enter login id:"),input("enter password: "))

print("login successfully")




# In[29]:


food = ["Tandoori Chicken", "Vegen Burgur","Truffle cake"]
pices = [4,1,"5gm"]           
price = [240,320,900] 

myorderFood =[]
myorderQuantity =[]
myorderCost =[]

print("welcome to zomato")
order = input("Can I take your order?: ")
if order == "no":
    exit()
else:
    print("Thank You")
    
foodOrder = input("Please Enter item")
if foodOrder == "Tandoori Chicken":
    myOrderFood.append(food[0])
    myOrderQuantity.append(pices[0])
    myorderCostappend =(price[0])
    
elif foodOrder == "Vegen Burgur":
    myOrderFood.append(food[1])
    myOrderQuantity.append(pices[1])
    myorderCostappend =(price[1])
    
    
elif foodOrder == "Truffle cake":
    myOrderFood.append(food[2])
    myOrderQuantity.append(pices[2])
    myorderCostappend =(price[2])
    
       
else:
    print("place order")
        

    
    


# In[ ]:


#Admin panle
class login:
    def __init__(self,id,pas):
        self.id = id
        self.pas = pas
        
    def check(self, id, pas):
        
        if self.id == id and self.pas == pas:
              return self.id,self.pas
            
log = login(" "," ")
log.check(input("enter login id:"),input("enter password: "))

print("login successfully")




# In[14]:


# Admin panl
food = ["Tandoori Chicken", "Vegen Burgur","Truffle cake"]
new_food = input("Please enter the new food item: ")
food.append(new_food)
print("updated food item list:",food)


# In[17]:


pices = [4,1,"5gm"]         
new_pices = input("Please enter the new pices: ")
pices.append(new_pices)
print("updated pices list:",pices)


# In[19]:


price = [240,320,900]
new_price = input("Please enter the new price: ")
price.append(new_price)
print("updated price list:",price)


# In[20]:


print("updated lists:",food,pices,price)


# In[6]:


food = ["Tandoori Chicken", "Vegen Burgur","Truffle cake"]
food.remove("Tandoori Chicken")
print("updated food list:",food)


# In[ ]:




