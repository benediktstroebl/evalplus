
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    range_l = min(x, y)
    range_u = max(x, y) + 1
    for num in range(range_l, range_u):
        if num % 2 == 0 and x < y:
            return num
        if num % 2 == 0 and y > x:
            return num
    return -1

