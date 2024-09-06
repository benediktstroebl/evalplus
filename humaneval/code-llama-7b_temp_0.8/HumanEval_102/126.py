
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if (x < 1 or y < 1):
        return -1

    if (x % 2 != 0 or y % 2 != 0):
        if x > y:
            x, y = y, x

        if (x % 2 == 0):
            return x
        if (x + 2 <= y):
            return x + 2
        else:
            return -1
    else:
        if (x > y):
            x, y = y, x
        if (x % 2 == 0):
            return x
        if (x + 2 <= y):
            return x + 2
        else:
            return -1
