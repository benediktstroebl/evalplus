
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    min_num = max(x, y)
    max_num = min(x + y, 2 * x + y)
    result = max_num // 2
    if max_num % 2 == 0:
        return result
    else:
        return -1
