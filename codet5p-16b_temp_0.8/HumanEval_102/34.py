
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x <= 0 or y <= 0:
        return -1
    max_num = min(x, y)
    for num in range(max_num, 0, -1):
        if num % 2 == 0 and num <= y and num >= x:
            return num
    return -1

