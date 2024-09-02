
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    a = (x + y) // 2
    b = (x + y) // 2
    if (x <= 0) or (y <= 0):
        return -1
    else:
        if (a % 2 == 0) and (a <= y) and (a >= x):
            return a
        else:
            return choose_num(x, b - 1)
