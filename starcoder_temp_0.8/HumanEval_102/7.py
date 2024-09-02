
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # check if x is even
    if (x % 2 == 0):
        # check if y is even
        if (y % 2 == 0):
            # check if y is bigger
            if (y > x):
                return y - 2
            # check if y is smaller
            else:
                return x - 2
        # y is odd
        else:
            return x - 1
    # x is odd
    else:
        # check if y is even
        if (y % 2 == 0):
            return y - 1
        # y is odd
        else:
            return -1
