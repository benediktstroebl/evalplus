
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n == 0:
        return x
    elif n == 1:
        return y
    elif n == 2:
        return x_or_y(n-1, y, x_or_y(n-1, x, y))
    else:
        if n % 2 == 0:
            return x_or_y(n-1, x, x_or_y(n-1, x, y))
        else:
            return y_or_x(n-1, x, y)
        
