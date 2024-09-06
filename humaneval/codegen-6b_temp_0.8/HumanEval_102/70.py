
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Hint: you can use the // operator to divide two numbers and the % operator to
    #       find the remainder.
    if (y < x):
        return -1
    while (y > 0):
        if (y % 2 == 0 and (y - x) % 2 == 0):
            return y
        y = y - 1
    return -1
