
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n % 2 == 0:
        # n is even, so the result should be x
        return x
    elif n % 3 == 0:
        # x is the result for n = 3x + 1
        return x
    else:
        # n is odd, so the result should be y
        return y
