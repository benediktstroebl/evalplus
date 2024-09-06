
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    min_num = min(x,y)
    max_num = max(x,y)
    num = 1
    while num <= max_num:
        if (num % 2 == 0) and (num >= min_num):
            return num
        num += 1 
    return -1
