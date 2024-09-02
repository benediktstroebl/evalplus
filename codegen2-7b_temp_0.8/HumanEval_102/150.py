
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2!= 0 or y % 2!= 0:
        return -1
    
    smaller = min(x, y)
    larger = max(x, y)
    
    for i in range(larger, smaller - 1, -2):
        if i % 2 == 0 and i >= x and i <= y:
            return i
    
    return -1

