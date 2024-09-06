
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x_abs = abs(x)
    y_abs = abs(y)

    if x_abs <= y_abs:
        return -1

    if x_abs % 2 == 0 and y_abs % 2 == 0:
        return x_abs
    else:
        return y_abs
