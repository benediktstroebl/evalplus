
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < y:
        x, y = y, x
    x_list = list(range(x, y+1, 2))
    for i in x_list:
        if x_list.count(i) == 2:
            return i
    return -
