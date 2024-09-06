
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    #return x if n%x!=0 or n%y==0 else y
    #if n%x == 0 or n%y == 0:
    #    return y
    #else:
    #    return x
    return x if not(n % x) or n % y == 0 else y
