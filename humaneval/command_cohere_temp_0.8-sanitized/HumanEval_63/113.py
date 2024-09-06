def fibfib(n):
    a,b,c = 0,0,1
    for _ in range(n-3):
        a,b,c = b,c, a+b+c
    return c