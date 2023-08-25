Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 7+3*2
print (x)
13
print ('p \n E \n D \n A \n S')
p 
 E 
 D 
 A 
 S
print ('p \n E \n M \n D \n A \n S')
p 
 E 
 M 
 D 
 A 
 S
x = (7+3)*2
print (x)
20
a = 20
b = 10
c = 15
d = 5
e = 0
e = (a+b)*c\d #(30*15)/5
SyntaxError: unexpected character after line continuation character
e = (a+b)*c/d #(30*15)/5
print("value of (a+b)*c/d is",e)
value of (a+b)*c/d is 90.0
e =(a+b)*(c/d); #(30)*(15/5)
print(e)
90.0
e =((a+b)*c)/d
print(e)
90.0
e =(a+b)*(c/d)
print(e)
90.0
#Adedeji Adetayo
#comment.py
#write a python program to add numbers
#program purpose: To explain comments
#Date: 2nd February,2023
a=10 #assigning value to the variable
b=20 #assigning value to the variable
x = a+b
print (x)
30
>>> 5==5
True
>>> 5==6
False
>>> z = (5==5)
>>> print (z)
True
>>> y = (5==6)
>>> print (y)
False
>>> a = 3
>>> if a>2:
...     print(a,"is greater")
...     print("done")
... 
...     
3 is greater
done
>>> a = -1
>>> if a<0:
...     print(a,"a is smaller")
...     print ("finish")\
... 
... 
...           
-1 a is smaller
finish
>>> a = 6
>>> if (a%2)== 1
SyntaxError: incomplete input
>>> a = 6
>>> if a % 2 == 1:
...     print (a, "is an odd number")
... 
...     
>>> if a % 2 == 1:
...     print (a, "is an odd number")
... else:
...     print(a, "is an even number")
... 
...     
6 is an even number
