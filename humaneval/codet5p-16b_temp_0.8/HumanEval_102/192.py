
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    max_num = y
    num = y
    if x > y:
        max_num = x
        num = x
    if max_num % 2 == 0:
        max_num -= 1
    while num!= max_num:
        num += 2
        if num > max_num:
            num = max_num
            break
        if num >= x and num <= y:
            return num
    return -1
