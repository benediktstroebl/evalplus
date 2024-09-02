
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    
    if x % 2 == 0:
        biggest_even = x
    else:
        biggest_even = -1
        
    if y % 2 == 0:
        smallest_odd = y
    else:
        smallest_odd = -1
        
    if smallest_odd > biggest_even:
        biggest_even = -1
        
    return biggest_even
