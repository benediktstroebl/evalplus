
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    max_y = int(y / 2)
    if x < y and y % 2 == 0:
        return x
    elif x < y and y % 2 == 1:
        return y
    else:
        return choose_num(x + 1, max_y) if (x + 1) * 2 <= y else choose_num(x, max_y)
