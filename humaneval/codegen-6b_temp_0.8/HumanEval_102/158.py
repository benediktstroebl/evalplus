
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    cond1 = x % 2 == 0
    cond2 = y % 2 == 0
    help_value = None
    if cond1 and cond2:
        help_value = -1
    elif cond1 or cond2:
        help_value = -1
    elif x == y:
        help_value = -1
    else:
        help_value = (x + y - 1) / 2
    return help_value
