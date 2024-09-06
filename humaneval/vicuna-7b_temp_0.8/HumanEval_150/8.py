
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    n = int(n)
    if n == 2:
        return n
    elif n % 2 == 0:
        return y
    elif not (y % (n // 2)):
        return y
    else:
        return x

x_or_y(1000, x, y)