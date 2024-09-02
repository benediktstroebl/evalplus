
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    
    if n == 1:
        raise ValueError("n should not be 1.")
    elif not is_prime(n):
        return x
    else:
        return y
    
