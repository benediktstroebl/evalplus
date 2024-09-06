
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Set num to a value that is higher than max possible and possible.
    num = x

    # Check if the integer is greater than possible and update num that
    # corresponds with possible.
    if x % 2 == 0 and x >= y:
        num = x

    # Check if the integer is greater than possible, but not greater than
    # possible + one, and update num that corresponds with possible.
    if x % 2 == 0 and x > y - 1:
        num = y - 1

    return num
