
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    else:
        max_num = -1
        while x <= y:
            if (x % 2 == 0) and (max_num == -1):
                max_num = x
            if (x % 2 == 0) and (x > max_num):
                max_num = x
            x = x + 1
        return max_num
