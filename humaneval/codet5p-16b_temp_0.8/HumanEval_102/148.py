
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    max_num = 0
    while x < y:
        if x % 2 == 0 and x > max_num:
            max_num = x
        x += 1
    if max_num == 0:
        return -1
    return max_num

