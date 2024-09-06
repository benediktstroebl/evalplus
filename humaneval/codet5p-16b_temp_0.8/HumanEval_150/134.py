
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n == 1:
        return x
    elif n == 2:
        return y
    elif n == 3:
        return x + y
    elif n == 4:
        return x + y + 1
    elif n == 5:
        return x + y + 2
    elif n == 6:
        return x + y + 3
    elif n == 7:
        return x + y + 4
    elif n == 8:
        return x + y + 5
    elif n == 9:
        return x + y + 6
    elif n == 10:
        return x + y + 7
    elif n == 11:
        return x + y + 8
    elif n == 12:
        return x + y + 9
    elif n == 13:
        return x + y + 10
    elif n == 14:
        return x + y + 11
    elif n == 15:
        return x + y + 12
    elif n == 16:
        return x + y + 13
    elif n == 17:
        return x
