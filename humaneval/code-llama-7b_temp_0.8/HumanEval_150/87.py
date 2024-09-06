
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    while (n != 1):
        if (n % 2 == 0) and (n % 3 == 0):
            n /= 2
            n /= 3
        elif (n % 2 == 0):
            n /= 2
        elif (n % 3 == 0):
            n /= 3
        else:
            break
    if n == 1:
        return x
    else:
        return y

