def fibfib(n):
    a,b = 0,1
    for i in range(n-2):
        a,b = b, a+b
    return b