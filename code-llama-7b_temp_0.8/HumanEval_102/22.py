
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y%2 == 1:
        y += 1
    if x%2 == 0:
        if y - x > 1:
            return -1
        else:
            return y
    if y - x <= 2:
        if y - x == 0:
            return y
        elif y - x == 1:
            return y
        elif y - x == 2:
            return y
    else:
        return -1

