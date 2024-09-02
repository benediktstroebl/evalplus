
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    import math as m
    
    if n == 1: return x
    elif (x%2 == 0 and y%2 == 0): return x_or_y(n - 1, x/2, y/2)
    elif (x%2 != 0 and y%2 != 0): return x_or_y(n - 1, (x + 1)/2, (y + 1)/2)
    else: return x_or_y(n - 1, x, y)

