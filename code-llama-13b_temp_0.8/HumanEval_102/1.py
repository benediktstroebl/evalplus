
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y <= x:
        return -1
    if x%2 == 0:
        if y%2 == 0:
            if y-x <= 2:
                return max(x,y)
            else:
                return x + 2*((y-x)//2)
        else:
            return x + 2*((y-x)//2)
    else:
        if y%2 == 0:
            return x + 2*((y-x-1)//2)
        else:
            if y-x <= 1:
                return -1
            else:
                return x + 2*((y-x-1)//2)
        
        
