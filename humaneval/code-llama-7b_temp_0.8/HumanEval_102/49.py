
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # print("choose_num(x={}, y={})".format(x, y))
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    # print("choose_num(x={}, y={})".format(x, y))
    for i in range(x, y):
        if i % 2 == 0:
            return i
    return -1
