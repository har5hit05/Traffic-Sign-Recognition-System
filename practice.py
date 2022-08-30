"""from array import *                          #add elements of array & search a particular element

arr = array('i' , [])

n = int(input("enter length of array"))

for i in range(n):
    x = int(input("enter next element"))
    arr.append(x)

print(arr)

val = int(input("enter value to be searched"))

k=0
for e in arr:
    if e==val :
        print(k)
        break
    k=k+1

else:
    print("element not found") """



"""av = 10
x= int (input("how many candies do u want?"))                   # CANDY MACHINE
i=1

while i<=x :
   if i>av :
    print("out of stock")
    break

   print("candy")
   i=i+1

print("BYE") """


from array import *
from numpy import *

#m1 = matrix(['1 2 3 : 4 5 6 : 13 14 15'])
#m2 = matrix('7 8 9: 10 11 12:16 17 18')
#print(m1)

"""
a = input("enter string")
b = input()
c = b.split("#")
for i in range(c):
    for j in range (len(c)):
        if j + c[j]== a :
            print(i)
            print(c[j])
            break """


"""m = matrix(('1 2 3 4 ; 5 6 7 8'))                # MATRIX
print(m)
print(diagonal(m))
print(m.max())"""

"""def sum(a,*b):
    c = a
    for i in b:
        c = c+i
    print(c)

sum(34,45,67,78)"""

"""lst = []
n = int(input("enter no of elements:"))

for i in range(n):
    x=input("enter next element")
    lst.append(x)"""


def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even = even + 1

        else:
            odd = odd +1

    return even,odd


lst = [21,23,43,45,65,76,87,62]
print(lst)
even,odd = count(lst)
print("Even:{} and Odd:{}".format(even,odd))