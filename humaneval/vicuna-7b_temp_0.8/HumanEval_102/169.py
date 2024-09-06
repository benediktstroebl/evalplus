
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y - x <= 2:
        return -1
    x_range = range(x, y + 1)
    max_even = max(x_range)
    if max_even % 2 == 0:
        return max_even
    else:
        return -1
