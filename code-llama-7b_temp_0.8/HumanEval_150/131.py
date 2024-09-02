
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    if x % 2 == 0:
        x += 1
    if x == n:
        return y
    if n % x == 0:
        return y
    return x_or_y(n, x + 2, y)

