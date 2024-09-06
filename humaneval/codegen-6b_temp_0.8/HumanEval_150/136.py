
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    pass
    # IMPLEMENT THIS
    
    if n % 2 == 0:
        return x
    if n % 3 == 0:
        return y
    
    if n % 5 == 0:
        return x
    if n % 7 == 0:
        return y
    
    return n
    
    
