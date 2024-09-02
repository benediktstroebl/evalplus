
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    N = x_or_y.n
    if n == 2 or n == 3:
        return n
    if (n % 2 == 0):
        return y
    elif (n % 3 == 0):
        return x
    i = 5
    while (i * i <= n):
        if (n % i == 0):
            return y
        i = i + 2
    x_or_y.n = x_or_y.n + 1
    return x

