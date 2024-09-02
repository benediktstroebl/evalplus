
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x == y:
        return x
    elif y == 1:
        return -1
    elif x == 0:
        return 2
    elif y % 2 == 0:
        return y
    elif y % 2 == 1:
        return x

    while True:
        if y % 2 == 0:
            return y
        elif x > y:
            return -1
        x += 2
        y += 1

