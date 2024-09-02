
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    def x_or_y_helper(n, x, y):
        if n == 1:
            return x if is_prime(x) else y
        return x_or_y_helper(n-1, y, x)
    return x_or_y_helper(n, x, y)
