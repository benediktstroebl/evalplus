
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x <= 0 or y <= 0:
        return -1
    elif x > y:
        return -1
    elif x % 2 == 1 and y % 2 == 1:
        return -1
    elif x % 2 == 1:
        x += 1
    elif y % 2 == 1:
        y -= 1
    if x == y:
        return x
    if (y - x) <= 2:
        return y
    if (y - x) % 2 == 0:
        return y - 2
    return y - 1

