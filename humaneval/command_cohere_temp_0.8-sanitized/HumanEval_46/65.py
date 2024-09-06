def fib4(n):
    a,b,c,d = 0,0,1,0
    for i in range(n):
        a,b,c,d = d,a,b+c+d,a+b+c
    return d