
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        if n % 2 == 0:
            return y
        else:
            return x
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 5:
        return 5
    elif n == 7:
        return 7
    elif n == 11:
        return 11
    elif n == 13:
        return 13
    elif n == 17:
        return 17
    elif n == 19:
        return 19
    elif n == 23:
        return 23
    elif n == 29:
        return 29
    elif n == 31:
        return 31
    elif n == 37:
        return 37
    elif n == 41:
        return 41
    elif n == 43:
        return 43
    elif n == 47:
        return 47
    elif n == 53:
        return 53
    elif n == 59:
        return 59
    elif n == 61:
        return 61
    elif n == 67:
        return 67
    elif n == 71:
        return 71
    elif n == 73:
        return 73
    elif n == 79:
        return 79
    elif n == 83:
        return 83
    elif n == 89:
        return 89
    elif n == 97:
        return 97
    elif n == 101:
        return 101
    elif n == 103:
        return 103
    elif n == 107:
        return 107
    elif n == 109:
        return 109
    elif n == 113:
        return 113
    elif n == 127:
        return 127
    elif n == 131:
        return
