
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y <= x:
        return -1
    if x % 2 == 0:
        low = x
    else:
        low = x + 1
    if y % 2 == 0:
        high = y
    else:
        high = y - 1
    while low <= high:
        tmp = (low + high) / 2
        if tmp >= x and tmp <= y and tmp % 2 == 0:
            return tmp
        elif tmp < x:
            low = tmp + 1
        else:
            high = tmp - 1

