def pypart(n):
    #outer loop to handle number of rows
    # n in this case
    for i in range(0,n):
        # inner loop to handle number of columns
        #value changing acc. to outerloop.
        for j in range(0,i+1):
            print("*",end=" ")
        #ending line after each row
        print("\r")
def pypart2(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
def pypart3(n):
    # 180 degrees rotation.
    k = 2*n-2
    for i in range(0,n):
        #inner loop to handle spaces
        # values changing acc. to requirement
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        #inner loop handle number of columns
        #values changing acc. to outerloop
        for j in range(0,i+1):
            print("*",end = " ")
        print("\r")

def triangle(n):
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end= " ")
        k = k - 1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
def numpart(n):
    num = 1
    for i in range(0,n):
        num = 1
        for i in range(0,i+1):
            print(num,end=" ")
            num = num + 1
        print("\r")
        #do without re-assig .
def alphapat(n):
    num = 65
    for i in range(0,n):
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end=" ")
        num = num+1
        print("\r")
        #do continous alphabetes
n = 10
pypart(n)
pypart2(n)
pypart3(n)
triangle(n)
numpart(n)
alphapat(n)
