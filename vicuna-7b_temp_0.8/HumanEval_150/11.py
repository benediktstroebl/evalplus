
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Check if n is prime
    if n > 1 and (n % 2) == 0:
        return y
    if n > 1 and (n % 3) == 0:
        return x
    # Try to divide n by 4
    if n % 4 == 0:
        return y
    # Try to divide n by 5
    if n % 5 == 0:
        return x
    # Try to divide n by 6
    if n % 6 == 0:
        return y
    # Try to divide n by 7
    if n % 7 == 0:
        return x
    # Try to divide n by 8
    if n % 8 == 0:
        return y
    # Try to divide n by 9
    if n % 9 == 0:
        return x
    # Try to divide n by 10
    if n % 10 == 0:
        return y
    # If we reach this point, n is prime
    return x
