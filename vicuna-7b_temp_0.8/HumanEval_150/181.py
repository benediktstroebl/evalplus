
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 2:
        return n
    elif n % 2 == 0:
        return y
    elif n % 3 == 0:
        return y
    elif n % 3 == 1:
        return x
    else:
        for i in range(4, int(n**0.5) + 1):
            if n % i == 0:
                return y
        return x

x_or_y(50, 34, 12)
