
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 1 and y % 2 == 1:
        i = 1
        while (i <= x and i <= y):
            if (i % 2 == 0):
                i += 1
            elif (x < y and i % 2 == 1):
                if (x - i == 0 or y - i == 0):
                    return i
                i += 1
            elif (x > y and i % 2 == 0):
                if (x - i == 0 or y - i == 0):
                    return i
                i += 1
    elif x % 2 == 1 and y % 2 == 0:
        return -1
    elif x % 2 == 0 and y % 2 == 1:
        return -1
    else:
        return -1


