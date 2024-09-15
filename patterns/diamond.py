n=int(input())

p=1
for i in range(1,n+1):


    for k in range(n,i-1,-1):
        print(" ",end=" ")

    
    for j in range(1,p+1):
        print("*",end=" ")

    p+=2
    print("\n")
p=(n*2)-1
for i in range(n,0,-1):

    for k in range(i,n+1):
        print(" ",end=" ")

    
    for j in range(p,0,-1):
        print("*",end=" ")

    p-=2
    print("\n")