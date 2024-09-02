
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return x
    if n == 2:
        return x
    if n == 3:
        return y
    else:
        return x_or_y(n - 1, y, x) or x_or_y(n - 2, x, y) or x_or_y(n - 3, y, x)
