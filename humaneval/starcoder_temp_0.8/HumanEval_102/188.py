
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    biggest = max(x, y)
    smallest = min(x, y)
    if biggest % 2 == 0:
        return biggest
    else:
        i = biggest - 1
        while i >= smallest:
            if i % 2 == 0:
                return i
            else:
                i -= 1
    return -1
