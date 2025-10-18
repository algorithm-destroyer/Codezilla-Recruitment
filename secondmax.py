# THIS PROGRAM WORKS FOR BOTH +VE AND -VE ELEMENTS OF ARRAY
n = int(input("Enter number of elements of array: "))
l = []
for i in range(1,n+1):
    a = int(input(f"Enter number {i}: "))
    l.append(a)
lar = max(l); mini = min(l)
for i in l:
    if i == lar:
        continue
    else:
        if i > mini:
            mini = i
print(f"The second largest number in the array is {mini}.")