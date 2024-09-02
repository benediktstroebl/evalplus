
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if (n in [2, 3, 5, 7, 11]):
        return x
    elif (n in [13, 17, 19, 23, 29]):
        return y
    else:
        return -1

