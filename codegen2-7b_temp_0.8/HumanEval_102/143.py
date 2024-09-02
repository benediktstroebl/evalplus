
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    for x1 in range(x, y + 1):
        for y1 in range(x, y + 1):
            if x1 % 2 == 0 and y1 % 2 == 0:
                return min(x1, y1)
    return -1
