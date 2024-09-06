
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x = int(x)
    y = int(y)
    num_range = range(x, y+2)

    if x % 2 == 0 and y % 2 == 0 and x < y:
        if x in num_range and y in num_range:
            return None
        else:
            return -1

    elif x % 2 == 0 and y % 2 != 0:
        if x not in num_range:
            return -1
        else:
            return x

    elif x % 2 != 0 and y % 2 == 0:
        if y not in num_range:
            return -1
        else:
            return y

    else:
        return -1


