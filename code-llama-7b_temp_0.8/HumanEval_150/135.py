
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return None
    if n <= 3:
        return n
    if n % 2 == 0 or n % 3 == 0:
        return y
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return y
        i += 6
    return x

