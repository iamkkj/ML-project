def prime(n):
    x=int(n**0.5)+1
    t=0
    for i in range(1,x):
        if n%i==0:
            t+=1
    if t==1:
        return True
    else:
        return False
for i in range(100,301):
    if prime(i):
        print(i,end=" ")
