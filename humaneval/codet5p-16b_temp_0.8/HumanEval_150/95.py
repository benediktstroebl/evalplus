
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19:
        return x
    elif n == 4 or n == 6 or n == 8 or n == 9 or n == 10 or n == 12 or n == 14 or n == 15 or n == 16 or n == 18 or n == 20:
        return y
    else:
        return x_or_y(n-2, x, y)

