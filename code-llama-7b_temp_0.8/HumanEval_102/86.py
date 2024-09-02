
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if (x % 2 != 0) or (y % 2 != 0):
        raise ValueError('x and y should be even numbers')
    
    if y <= x:
        return -1
    
    z = x
    while z < y:
        z += 2
        if z >= x and z <= y and (z % 2 == 0):
            return z
    return -1
