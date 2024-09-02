
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if not isinstance(n, int) or not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("x_or_y takes 3 integers arguments")
        
    return x if is_prime(n) else y

