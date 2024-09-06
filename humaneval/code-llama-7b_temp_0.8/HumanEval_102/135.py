
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if not x <= y:
        raise ValueError(f"x: {x} must be <= y: {y}")
    if not isinstance(x, int):
        raise TypeError(f"x: {x} must be an integer")
    if not isinstance(y, int):
        raise TypeError(f"y: {y} must be an integer")
    if not x > 0:
        raise ValueError(f"x: {x} must be a positive number")
    if not y > 0:
        raise ValueError(f"y: {y} must be a positive number")
    return int((x + y)/2) * 2
