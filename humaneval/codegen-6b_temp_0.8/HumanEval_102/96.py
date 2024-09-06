
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x_str = str(x)
    y_str = str(y)
    # find the biggest even number in the range [x, y]
    if int(x_str) % 2 == 0:
        if int(y_str) % 2 == 0:
            return int(x_str)
        else:
            return int(y_str)
    else:
        if int(y_str) % 2 == 0:
            return int(y_str)
        else:
            return -1

