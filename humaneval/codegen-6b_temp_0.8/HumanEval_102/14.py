
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 0:
        x = x // 2
    if y % 2 == 0:
        y = y // 2
    while x <= y:
        if x % 2 == 0:
            x = x // 2
        else:
            break
    while y >= x:
        if y % 2 == 0:
            y = y // 2
        else:
            break
    if x > y:
        return -1
    else:
        return x
