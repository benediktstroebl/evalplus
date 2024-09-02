
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Test whether n is prime
    if n == 2:
        return x
    elif n == 3:
        return y
    elif n % 2 == 0:
        return y
    elif n > 3 and (n % 2) == 1:
        return x
    elif n > 4 and n % 3 == 0:
        return y
    else:
        return x
