
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # define some constants
    q = 2
    sq = q**2
    phi = (1 + math.sqrt(5))/2
    p = 2
    i = 0
    while (p**2 - p + 1 == sq*i and p != i):
        p = p + 1
        i = i + 1
    if p**2 - p + 1 == sq*i:
        return x
    else:
        return y