list1 = [4,56,25,32,85,63]
for i in range(len(list1)):
    for j in range(0,len(list1)-i-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
print(list1)
n = 32
for i in range(len(list1)):
    for j in range(0,len(list1)-i+1):
        if list1[i] == n:
            print("found",list1[i],"at index",i)
            break
