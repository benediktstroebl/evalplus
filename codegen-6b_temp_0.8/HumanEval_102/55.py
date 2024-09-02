
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # your code here
    
    while True:
        x = x+1
        if x % 2 == 0:
            if x >= y:
                break
            else:
                continue
        else:
            if x >= y:
                break
            else:
                continue
    
    if x == y:
        return x
    else:
        return -1
    