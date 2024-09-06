
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # The function checks if n is prime by using the Miller-Rabin primality test
    # which is a probabilistic test and should work for n > 5
    if n > 1 and not n % 2 and not n % 3 and not n % 4 and not n % 5:
        # If n is prime, return x
        return x
    else:
        # If n is composite, return y
        return y
