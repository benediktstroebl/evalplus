
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n > 0:
        return y if n == 2 else x
    elif n == 0:
        return x if x % 2!= 0 else y
    else:
        return y if n == 2 else x

