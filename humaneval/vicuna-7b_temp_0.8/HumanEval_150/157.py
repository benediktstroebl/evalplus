
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # initialize variables
    p = 2
    while p <= n:
        if n % p == 0:
            break
        p += 2
    if n % p == 0:
        return y
    else:
        return x