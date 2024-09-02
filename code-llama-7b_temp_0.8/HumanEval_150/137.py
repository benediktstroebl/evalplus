
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Please print out which test case you're on when you test your code!
    print 'Case #{0}: {1}'.format(n, x) if is_prime(n) else 'Case #{0}: {1}'.format(n, y)
