
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    # n is a prime number
    if n > 1:
        # if n is even and greater than 2, n is not a prime number
        if n > 2 and n % 2 == 0:
            return y
        # if n is odd, it is a prime number
        else:
            return x

    # n is not a prime number
    else:
        return y
