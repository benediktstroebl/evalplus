
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2!= 0 or y % 2!= 0:
        return -1

    x = int(x / 2)
    y = int(y / 2)

    result = 0

    for i in range(x, y + 1):
        result = (result * 10) + i

    return result
