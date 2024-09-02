
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
    big = x
    small = y
    while x <= y:
        if x % 2 == 0:
            x += 1
        else:
            if big % 2 == 0:
                big += 1
            else:
                small = x + 1
                break
    return small

