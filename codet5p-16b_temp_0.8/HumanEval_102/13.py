
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    biggest_num = y
    for i in range(x, y + 1):
        if i % 2 == 0:
            if biggest_num < i:
                biggest_num = i
    if biggest_num == y:
        return -1
    return biggest_num
