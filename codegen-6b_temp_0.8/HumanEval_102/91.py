
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # in Matlab, x <= y means x < y (T/F)
    # this doesn't make sense when x and y are integers, however
    if x >= y:
        return -1
    
    # greedily find the biggest even number in [x, y]
    while x % 2 == 0:
        x = x / 2
    
    # y * 2 is too big: x + y * 2 = y * 3
    # y * 2 + 1 is too big: x + y * 3 = y * 4
    while x <= y:
        if x * 2 >= y * 3:
            y = y * 2
            if y % 2 == 0:
                return y
        else:
            x = x * 2
    
    return -1
        
        
