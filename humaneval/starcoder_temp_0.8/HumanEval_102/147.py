
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    x = x - 1
    y = y - 1
    #your code here
    z = 1
    if x % 2 == 0 and y % 2 == 0:
        while y >= x:
            if x % z == 0 and y % z == 0:
                return x
            z += 2
    else:
        return -1
    
    
