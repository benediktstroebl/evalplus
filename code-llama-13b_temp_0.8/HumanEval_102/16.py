
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # find the closest even number, and
    # check if it is in the range [x, y]
    return -1 if x % 2 != 0 or y % 2 != 0 or x > y else max(x, y) & ~1 if x // 2 == y // 2 else max(x, y) - 1
