
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 0:
        min = x
    else:
        min = x + 1
    
    if y % 2 == 0:
        max = y
    else:
        max = y - 1
    
    for n in range(min, max+1, 2):
        if n % 2 == 0:
            return n
    return -1
