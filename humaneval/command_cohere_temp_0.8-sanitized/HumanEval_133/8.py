def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Round each list item to the nearest higher integer before squaring.
    """
    return sum(x ** 2 for x in lst if isinstance(x, int))