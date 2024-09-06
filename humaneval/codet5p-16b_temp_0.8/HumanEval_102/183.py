
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    num = 0
    max_num = y
    if x % 2 == 0 and x <= y:
        num = x
        max_num = y
    if x > y:
        num = -1
    else:
        while num < x:
            num += 2
        if num > max_num:
            num = -1
    return num
