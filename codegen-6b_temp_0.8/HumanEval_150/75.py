
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return x_or_y(n // 2, x, y)
    elif n % 3 == 0:
        return x_or_y(n // 3, x, y)
    elif n % 5 == 0:
        return x_or_y(n // 5, x, y)
    else:
        return y

