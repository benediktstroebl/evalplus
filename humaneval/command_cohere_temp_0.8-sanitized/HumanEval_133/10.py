def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Round each list element to the nearest higher integer before squaring.
    """
    return sum((int(rounding(x))**2 for x in lst))
def rounding(x):
    """
    Round the given number to the nearest higher integer.
    """
    return int(x + 1) if x % 1 == 0.5 else int(x)