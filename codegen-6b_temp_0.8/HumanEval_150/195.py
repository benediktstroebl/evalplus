
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Python 2 code:
    # return x if n%2==0 else y

    # Python 3 code:
    return x if n%2==0 else y


__author__ = "Matt Krzysztof Skoczenik"
__copyright__ = "Copyright 2017 Matt Krzysztof Skoczenik"
__license__ = "Apache License, Version 2.0"
__version__ = "0.1"
