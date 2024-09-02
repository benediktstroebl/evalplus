
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        bigger_num = x
        smaller_num = y
    else:
        bigger_num = y
        smaller_num = x
    for i in range(smaller_num, bigger_num + 1):
        if i % 2 == 0 and i in range(x, y + 1):
            return i

