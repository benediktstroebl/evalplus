
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    # check if n is prime
    if n % 2 == 1:
        # check if n is divisible by any odd number
        if n % 3 == 0:
            return x
        else:
            return y
    else:
        # check if n is divisible by 4
        if n % 4 == 0:
            return x
        else:
            return y
