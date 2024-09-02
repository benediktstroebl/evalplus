
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < y:
        return -1
    if x % 2 and y % 2:
        return -1
    if x % 2:
        return y - x + 1
    if y % 2:
        return y - x
    if x == y:
        return -1
    while True:
        if x <= y:
            if x % 4 == 0:
                return x
            if y % 4 == 0:
                return y
            if x % 2 and y % 2:
                return -1
            if x % 2:
                return y - x + 1
            if y % 2:
                return y - x
            x += 2
            y += 2
        else:
            if x % 4 == 0:
                return x
            if y % 4 == 0:
                return y
            if x % 2 and y % 2:
                return -1
            if x % 2:
                return y - x + 1
            if y % 2:
                return y - x
            y += 2
            x += 2
