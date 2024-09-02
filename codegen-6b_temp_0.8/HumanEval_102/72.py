
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x == y:
        return -1
    else:
        if x < y:
            for index in range(x, y + 1):
                if index % 2 == 0:
                    return index
            return -1
        else:
            for index in range(y, x + 1):
                if index % 2 == 0:
                    return index
            return -1
