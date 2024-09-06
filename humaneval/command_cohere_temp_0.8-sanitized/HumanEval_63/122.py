def fibfib(n):
    a,b,c = 0,1,0
    for i in range(n):
        c = a+b+c
        a,b = b,c
    return c