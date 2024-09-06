
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    p = 2
    i = 2
    while (i * i <= n and p * p <= n):
        if (n % i == 0):
            break
        p = i
        i = i + 2
    if (p * p >= n):
        return y
    else:
        return x
