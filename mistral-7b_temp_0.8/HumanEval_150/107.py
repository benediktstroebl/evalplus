
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """


    # TODO: Use this code as a starting point for your solution.
    # As you can see, there are several problems with this code.
    # Fix these issues and add some comments to explain what you are doing.
    if n % 2 == 0:
        return y
    else:
        return x

