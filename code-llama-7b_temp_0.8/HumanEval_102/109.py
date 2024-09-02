
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Your code goes here.
    #x = int(x)
    #y = int(y)
    m = max(x,y)
    mi = min(x,y)
    if m % 2 == 0 and m <= mi:
        return m
    elif m % 2 != 0 and m - 1 <= mi:
        return m - 1
    else:
        return -1
    
