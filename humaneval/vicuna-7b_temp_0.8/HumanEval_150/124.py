
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    # Test for prime number
    if not is_prime(n):
        return y
    p = 2
    while p <= n/p - 1:
        if n % p == 0:
            return y
        p += 1
    return x
