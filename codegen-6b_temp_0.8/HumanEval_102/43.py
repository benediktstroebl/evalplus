
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # We assume that zero is valid
    if x == 0:
        return 0
    if y == 0:
        return -1
    while x < 0 or y < 0:
        if x < 0:
            x = abs(x)
        if y < 0:
            y = abs(y)
    while x > y:
        x = x - y
    # We check if the divisor is even    
    if x % 2 == 0:
        return x
    else:
        return -1
    
