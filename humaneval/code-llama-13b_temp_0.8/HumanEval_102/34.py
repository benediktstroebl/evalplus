
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y > x:
        x, y = y, x

    if x % 2 != 0:
        x += 1
    
    if x > y or y < 2:
        return -1
    
    return x
