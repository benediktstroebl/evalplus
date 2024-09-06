
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 1:
        x += 1
    if y % 2 == 1:
        y -= 1
    if x % 2 == 1 or y % 2 == 1:
        return -1
    num = y // 2
    for x in range(x, y + 1):
        if x % 2 == 0:
            num = x
            break
    return num

