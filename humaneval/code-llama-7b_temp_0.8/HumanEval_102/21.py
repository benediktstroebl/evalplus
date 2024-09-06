
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Choose even number from [x, y] range inclusive
    # If no such number return -1
    if x % 2 == 0:
        if x <= y <= x + 2:
            return x
        else:
            return -1
    elif y % 2 == 0:
        if x <= y:
            return y
        else:
            return -1
    else:
        return -1

