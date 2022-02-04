#!/usr/bin/env python
# coding: utf-8

# In[6]:


D = "Hello world, welcome to my code world"


# In[7]:


D


# In[11]:


print (D)


# In[16]:


a= "10.5"
print(a)
print(type(a))


# In[17]:


bool_var = "True"
print(bool_var)
print(type(a))


# In[18]:


bool_var = True
print(bool_var)
print(type(bool_var))


# In[21]:


var=10.6


# In[22]:


type(var)


# In[23]:


a=10
A=20

print(a)
print(A)


# In[24]:


string1= "hello"
print(string1)


# In[25]:


string1


# In[26]:


string2="hello world"


# In[28]:


string2


# # DATA TYPE

# In[37]:


name = "Diksha Lolekar"
gender = "Female"
address = "Nagpur, maharashtra"
age = 26


# In[32]:


type(name)


# In[36]:


type(age)


# #  OPERATORS
# 

# In[39]:


a=10
b=20


# In[40]:


a+b


# In[41]:


a-b


# In[42]:


a*b


# In[44]:


a/b


# In[45]:


print((4*5)-9+6/7)


# In[47]:


a%b


# In[48]:


a//b #Floor Division
         #Floor
         #Celling


# In[51]:


a%b #Modulus/Reminder


# # STRING

# In[56]:


a ='Ron'
b ='Wings'
c ='kate'


# In[57]:


print(a)
print(b)
print(c)


# In[61]:


print(type(a))
print(type(b))
print(type(c))


# In[62]:


print(len(a))
print(len(b))
print(len(c))


# In[75]:


str1 ="hello world" #strings are immutable


# In[76]:


str1[-1]


# In[77]:


str1[0:5]


# In[78]:


str1[1]


# In[80]:


str1[0:3]


# In[84]:


str1[3:]


# In[92]:


str1[::4]


# In[97]:


new_str =str1[0:2] + 'x'+ str1[-8:]


# In[98]:


str1


# In[99]:


new_str


# # CONCAT 

# In[89]:


first_name = "Ram"
last_name = "Verma"
print(first_name + last_name)
print(first_name + " "+last_name)


# # SLICING
#  #string[start:end:step]
#  

# In[101]:


string ='Hello World'


# In[102]:


string[2:5]


# In[103]:


string[-9:-6]


# In[104]:


string[1::2]


# In[105]:


string[0:5]


# In[108]:


string[6:11]


# # STRING METHODS

# In[110]:


#upper()
text = 'i have a cat'
print(text)


# In[113]:


text = 'i have a cat'
print(text.upper())


# In[115]:


# strips removes whitespace
#rstrip()
text = 'i have a cat'
print(text)
print(text.rstrip())
new_text = text.rstrip()


# In[124]:


len(text)


# In[125]:


text = '         i have a cat'
print(text)
print(text.rstrip())
new_text = text.rstrip()


# In[117]:


len(text)


# In[126]:


len(new_text)


# In[121]:


#lstrip
text = '                  i have a cat'
print(text)
print(text.lstrip())

new_text_lstripe = text.lstrip()


# In[123]:


len(text)


# In[128]:


len(new_text)


# In[133]:


text = '********587856787854#######'
print(text)
new_text = text.rstrip('#').lstrip('*')
print(new_text)


# In[134]:


#count()
text ='this is the sentence in this example'
print(text.count('is'))


# In[141]:


A = ' Data'
B = 'Analysis'
C = 'Python'

print('let us learn' + '{0} {1} using {2}'.format(A,B,C))


# In[144]:


input_var= 'bmaunmdbraai'
message1= input_var[0::2]
message2= input_var[1::2]

print(message1)
print(message2)
print(message1 + ',' + message2)


# # DATA STRUCTURE

# In[146]:


#Tuples
t= ('hello',2,3,4,5.5)


# In[147]:


t


# In[148]:


type(t)


# In[150]:


len(t)


# In[151]:


tuple1 = (1,2,4,'hello',(3,4,5))


# In[154]:


tuple2 =(3,4,5)
tuple2[1]


# In[159]:


tuple2 = (3,5,5, 'hello','world',(2,4,6))


# In[160]:


type(tuple2)


# In[161]:


len(tuple2)


# In[164]:


tuple2[5]


# In[179]:


#immutability
t= ("hello", "welcome",5,10,"world","of","analytics!!")


# In[170]:


t[3]


# In[184]:


t[0:2]


# In[181]:


t[-3:]


# In[186]:


new_tuple = t[0:2]+ ("to", "this")+ t[-3:]


# In[188]:


new_tuple


# In[190]:


tuple3 =(3,5,7,3,6,467,35,36,22,66,53,77)


# In[191]:


sorted(tuple3)


# In[193]:


#List
list1=["India",5,"Dehli"]


# In[194]:


list1


# In[196]:


print(type(list1))
print(len(list1))


# In[197]:


#Nested List
list2 = ["India", "Dehli", 5, 10, ["Rajkot", "Chennai"]]


# In[199]:


list2


# In[201]:


list2[0]


# In[202]:


list2[0:4]


# In[203]:


list2[0][4]


# In[204]:


#Indexing 
list2 = ["India", "Dehli", 5, 10, ["Rajkot", "Chennai"]]
list2[0]


# In[206]:


#Slicing
list2 = ["India", "Dehli", 5, 10, ["Rajkot", "Chennai"]]


# In[207]:


list2[-1]


# In[208]:


list2[4][0]


# In[209]:


#List Concat
list1 =[1,2,3,4]
list2 =[5,6,7,8]

new_list = list1+list2


# In[210]:


new_list


# In[211]:


#Add two element to an existing list
list3 =[1,2,3,4]
list4 =[5,6]
new_list = list3 + list4
new_list


# In[213]:


string1 ="hello how are you"
print("world" in string1)


# In[214]:


print("hello" in string1)


# In[216]:


#Membership in lists

list3 = [1,2,3,4]
print(1 in list3)
print(5 in list3)


# In[217]:


#Mutability
list1 = ["maths", "physics", "chemistry", "biology"]


# In[219]:


list1[3]= 'computer science'


# In[220]:


list1


# In[221]:


#Extend() Function

list1 = [1,2,3,4]
list1.extend([5,6])
list1


# In[222]:


#Append() Function
list1 = [1,2,3,4]
list1.append([5,6])
list1


# In[226]:


#del command

list2 = [1,2,3,4]
del list2[0]
list2


# In[228]:


#pop() - Deletes the last objects from the list
list3 = [1,2,3,4]
list3.pop(1)
list3


# In[230]:


#remove
list3 = [11,22,33,44]
list3.remove(33)
list3


# In[234]:


#sorting
A = ["orange", "mangoe","strawberry" ]
A.sort()
A


# In[233]:


A.sort(reverse=True)
A


# In[243]:


A = ["orange", "mango","strawberry" ]
B = A.sort()
print (A)
print (B)


# In[253]:


#shallow copy
A = ["orange", "mango","strawberry" ]
B = A
print(B)


# In[254]:


A.pop()


# In[250]:


A


# In[255]:


B 


# In[257]:


A = ["orange", "mango","strawberry" ]
B = A[:]
print(B)


# # OPERATORS
# 

# In[258]:


#binary operator
a = [1,2,30]


# In[259]:


12==12


# In[260]:


10==5


# In[261]:


10!=5


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




