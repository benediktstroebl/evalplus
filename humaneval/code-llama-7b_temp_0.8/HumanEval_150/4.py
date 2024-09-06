
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 1:
        raise ValueError("n should be a positive integer")
    
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("x and y should be integers")
    
    #if n is a prime number return x otherwise return y
    return x if is_prime(n) else y

