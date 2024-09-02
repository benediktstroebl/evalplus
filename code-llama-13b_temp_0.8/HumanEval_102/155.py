
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
    
    if x <= 2 and y <= 2:
        return 2
    
    if (x % 2 == 0) and (y % 2 == 0):
        if x <= y:
            return y
        else:
            return x
    
    if (x % 2 != 0) and (y % 2 != 0):
        if x < y:
            return choose_num(x + 1, y - 1)
        else:
            return choose_num(x - 1, y + 1)
        
    if (x % 2 == 0) and (y % 2 != 0):
        if x < y:
            return choose_num(x + 1, y)
        else:
            return choose_num(x, y - 1)

    if (x % 2 != 0) and (y % 2 == 0):
        if x < y:
            return choose_num(x, y + 1)
        else:
            return choose_num(x - 1, y)
    
    return -1

