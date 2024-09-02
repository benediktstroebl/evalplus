
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < 0 or y < 0:
        return -1
    elif x == y:
        return x
    elif y - x == 1:
        return y if x % 2 == 0 else -1
    elif x % 2 != 0:
        return choose_num(x + 2, y)
    elif y - x == 3:
        return choose_num(y - 2, y)
    else:
        return choose_num(x, (x + y) // 2)

