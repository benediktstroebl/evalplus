
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Introducing the variable which will store the value of x
    x_or_y = x
    
    # Introducing the variable which will store the value of y
    x_or_y1 = y
    
    # Here we check if the value of n is a prime number.
    for i in range(2, n):
        if (n % i) == 0:
            x_or_y = x_or_y1
            break
        else:
            x_or_y = x_or_y
    
    return x_or_y
