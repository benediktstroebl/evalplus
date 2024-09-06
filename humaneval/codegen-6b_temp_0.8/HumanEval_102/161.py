
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < y:
        return -1
    lower = max(x, y)
    upper = min(x, y)
    while lower % 2 == 0:
        lower /= 2
    while upper % 2 == 0 and upper != 1:
        upper /= 2
    if upper > 1:
        return -1
    else:
        num = lower
        while (lower <= upper):
            if (num % 2 == 0) and (num <= x):
                if num <= y:
                    return num
            if num < x:
                return -1
            num += 1
            

