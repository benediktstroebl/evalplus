
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    
    for n_prime in xrange(2, n):
        if n % n_prime == 0:
            if x == n_prime:
                return x
            else:
                return y
    return x
