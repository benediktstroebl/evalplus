
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y < x:
        return -1
    else:
        x = x % y
        y = y
        while x > 0:
            x = x % y
            y = y + y
        return y

