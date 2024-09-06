
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n % 2 == 0:
        return y
    if n > 2 and (n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        return x
    for p in range(3, int(n ** 0.5) + 1):
        if n % p == 0:
            return y
    return x
