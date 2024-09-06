
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # return x if x % 2 == 0 and x < y else -1
    # return y if y % 2 == 0 and y > x else -1
    # return -1 if y % 2 != 0 or y < x else x

    if x > 0 and y > 0 and y > x:
        if x % 2 == 0:
            return x
        elif y % 2 == 0:
            return y
        else:
            return -1
    else:
        return -1

