
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    biggest_even_in_range = -1
    if x < 0 or y < 0:
        return biggest_even_in_range
    
    for i in range(x, y+1):
        if i%2 == 0:
            if i >= biggest_even_in_range:
                biggest_even_in_range = i

    return biggest_even_in_range
