
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return x
    elif n == 2:
        return y
    elif n%2 == 0:
        return x_or_y(n//2, x, y)
    else:
        return x_or_y(n-1, x, y
