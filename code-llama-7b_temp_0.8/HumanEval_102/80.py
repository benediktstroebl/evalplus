
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    elif x % 2 != 0:
        x += 1
    elif y % 2 != 0:
        y -= 1
    if x > y:
        return -1
    while x % 2 == 0:
        x += 2
    while y % 2 == 0:
        y -= 2
    while x <= y:
        if x % 2 == 0:
            return x
        x += 2
    return -1
