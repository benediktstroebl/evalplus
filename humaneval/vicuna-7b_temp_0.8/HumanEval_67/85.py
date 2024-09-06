
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    n = int(n)
    a = s.split()
    if len(a)%2!=0:
        return -1
    b = [0] * n
    for i in range(n):
        b[i] = int(a[i])
    c = [0,0,0]
    for i in range(n):
        c[0] += b[i]
        c[1] += b[i]
        c[2] += b[i]
    d = [0] * n
    for i in range(n):
        d[i] = int(a[i])
    for i in range(n-1, -1, -1):
        d[i] += d[i+1]
    e = [0] * n
    for i in range(n):
        e[i] = d[i] - c[i]
    for i in range(n):
        if e[i] == 0:
            return -1
    return e[n-1]

