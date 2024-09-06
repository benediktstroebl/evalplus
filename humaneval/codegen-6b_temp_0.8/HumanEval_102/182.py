
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x >= y:
        return -1
    elif x == y:
        return x
    else:
        if y % 2 == 0:
            return y
        else:
            temp = min(x, y)
            if temp % 2 == 0:
                return temp
            else:
                return y - 1

