def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = d,a+b+c+d,c,a+b+c
    return a