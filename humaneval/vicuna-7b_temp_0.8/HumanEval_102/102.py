
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x_min, x_max = min(x, y), max(x, y)
    y_min, y_max = min(y, x), max(y, x)

    if x_min % 2 == 0 and x_max % 2 == 0:
        return x_max
    elif y_min % 2 == 0 and y_max % 2 == 0:
        return y_max
    else:
        return -1
