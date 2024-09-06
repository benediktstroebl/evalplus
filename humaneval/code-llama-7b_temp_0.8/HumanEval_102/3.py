
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    max = x
    if max % 2 != 0:
        max += 1
    if max < y:
        max += 2
    for i in range(max, y + 1, 2):
        if i >= x:
            return i
    return -1
