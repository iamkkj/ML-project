def armstrong(n):
    a=list(map(int,list(str(n))))
    t=0
    for i in a:
        t+=i**len(a)
    if n==t:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
armstrong(int(input()))
