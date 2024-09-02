
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Initialize variables to store the values of n and the result
    p, r = 2, 1
    while p <= n // 2:
        if n % p == 0:
            r, n = n, n - p
        p += 2
    return r
