
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y - x <= 1:
        return x
    while x < y:
        mid = x + (y - x) // 2
        if mid % 2 == 0:
            return mid
        x = mid + 1
    return -1
