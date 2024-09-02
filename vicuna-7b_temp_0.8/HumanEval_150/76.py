
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Check if n is a prime number
    if n % 2 == 1:
        # n is not a prime number
        return y
    elif n <= 3:
        # n is a prime number
        return x
    else:
        # Check if n is divisible by 3
        if n % 3 == 0:
            # n is not a prime number
            return y
        else:
            # n is a prime number
            return x
            
