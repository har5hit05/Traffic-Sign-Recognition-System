
n = int(input("enter the value of n"))
#i=1
#cnt = i
k = ord('A')

#print(k)

for i in range(n):
    for j in range(i+1):
        print(chr(k),end = " ")
    k=k+1

    print()
