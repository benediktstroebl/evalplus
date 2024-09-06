def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = b,c,d, a+b+c+d
    return a