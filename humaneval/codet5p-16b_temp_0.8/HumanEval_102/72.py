
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    num = x
    if y < x:
        num = y
    if x % 2 == 1 and num % 2 == 1:
        return -1
    else:
        while num >= x:
            if num % 2 == 0:
                return num
            num -= 1
        return -1
