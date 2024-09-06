
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    a = max(x, y)
    b = min(x, y)
    max_num = a
    if a % 2 == 0:
        max_num = a
    else:
        max_num = b
    
    while max_num >= b:
        if max_num % 2 == 0:
            max_num -= 1
        else:
            return -1
    return max_num
