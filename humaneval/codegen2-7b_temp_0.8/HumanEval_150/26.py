
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 0 or n == 1:
        return x
    elif n % 2 == 0:
        return x_or_y(n/2, y, x)
    else:
        return x_or_y(n*3+1, y, x)

