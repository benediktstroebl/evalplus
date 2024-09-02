
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        if (n % 2) == 0:
            return y
        elif (n % 3) == 0:
            return x
        else:
            for i in range(1, n-1):
                if (n % i) == 0:
                    return y
                elif (n % (i+1)) == 0:
                    return x
    else:
        return x

x_or_y(10, 5, 2)
