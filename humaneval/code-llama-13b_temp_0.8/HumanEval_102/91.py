
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    if x < 0 or y < 0:
        return -1
    if x > y:
        x, y = y, x
    
    if y - x + 1 <= 4:
        for i in range(x, y + 1, 2):
            if i % 2 == 0:
                return i
        return -1
    return -1

