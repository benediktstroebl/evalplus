
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Check if n is a prime number
    # If not, return y
    if n < 2:
        return y

    if n % 2 == 0:
        return x

    return x_or_y(3 * n + 1, x, y)

