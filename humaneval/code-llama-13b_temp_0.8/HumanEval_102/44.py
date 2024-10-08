
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y or x <= 0 or y <= 0:
        return -1
    if x % 2 == 0:
        x = x + 1
    if y % 2 == 1:
        y = y - 1
    for num in range(x, y + 1, 2):
        if num % 2 == 0:
            return num
    return -1

