
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # validate inputs
    if (x < 0 or y < 0 or x > y):
        raise ValueError("x and y must be positive and x <= y")
    if x % 2 != 0 or y % 2 != 0:
        raise ValueError("x and y must be even")

    if x == y:
        return -1

    res = 0
    if x <= y - 2:
        res = x + 2
    else:
        res = y - 1
    return res
