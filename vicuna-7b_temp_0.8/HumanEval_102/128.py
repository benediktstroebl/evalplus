
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y-x+1 in [x, y]:
        return x
    if y-x+1 in (y-x+2, y-x+3):
        return y-x+2
    return -1
