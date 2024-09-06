def fibfib(n):
    a,b,c = 0,1,1
    for _ in range(3,n+1):
        a,b,c = c,a+b,b+c
    return a