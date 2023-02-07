a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

for t in range(a,b):
    sum = 0
    for i in range(1,t):
        if t % i == 0:
            sum=sum+i
            i=i+1
    if sum == t:
        print(t,"is a perfect number")
    else:
        print(end=" ")
