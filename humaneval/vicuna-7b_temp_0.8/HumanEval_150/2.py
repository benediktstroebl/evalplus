
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # This is a simple program that uses a prime number checker
    # to check if the number n is a prime number. If it is,
    # it returns the value of x. Otherwise, it returns the value
    # of y.
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                return y
        return x