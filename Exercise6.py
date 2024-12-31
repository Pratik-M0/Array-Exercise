from array import *

value = array('i',[])

n = int(input("Enter the number of Elements in Array : "))

for i in range(n):
    print("Enter Element ", i+1 ," : ", end="")
    x = int(input())
    value.append(x)

print(value)

k=0

val = int(input("enter Element to find it's index number"))
for y in (value):
    if val==y:
        print("Index number of ", val, " is ", k)
    k+=1