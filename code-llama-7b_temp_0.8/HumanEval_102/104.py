
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if not isinstance(x, int):
        raise TypeError(f"'{x}' is not an int")
    if not isinstance(y, int):
        raise TypeError(f"'{y}' is not an int")
    if x < 0:
        raise ValueError(f"'{x}' is negative")
    if y < 0:
        raise ValueError(f"'{y}' is negative")
    if x > y:
        raise ValueError(f"'{x}' is greater than '{y}'")
    
    max_even = -1
    for i in range(x, y + 1):
        if i % 2 == 0:
            if i > max_even:
                max_even = i
    return max_even
