
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    if x < y:
        lower_num = x
        upper_num = y
    else:
        lower_num = y
        upper_num = x
        
    for num in range(lower_num, upper_num + 1):
        if num % 2 == 0:
            return num
    return -1
