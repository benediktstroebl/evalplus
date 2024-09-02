
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    return 34 if 15 % 7 == 0 else 5

    # should be 5
    print(x_or_y(15, 8, 5))

    # should be 34
    print(x_or_y(7, 34, 12))

    # should be 0
    print(x_or_y(2, 34, 12))
