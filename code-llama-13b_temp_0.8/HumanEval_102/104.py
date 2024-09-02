
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    result = -1
    if x <= y:
        x_mod = x % 2
        y_mod = y % 2
        if x_mod == y_mod == 0:
            result = y
        if y_mod == 0:
            result = y - 1
        if x_mod == 0:
            result = x
    return result
