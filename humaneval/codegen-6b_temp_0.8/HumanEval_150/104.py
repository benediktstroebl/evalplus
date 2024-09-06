
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return None
    if n == 2 or n == 3 or n == 5 or n == 7:
        return x
    if n%2 == 0:
        return y
    for i in range(3, int(math.sqrt(n))):
        if n % i == 0:
            return y
    return x 
    

