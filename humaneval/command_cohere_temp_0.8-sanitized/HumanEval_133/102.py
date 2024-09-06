def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Round each number to the nearest larger integer before squaring.
    """
    return sum(x ** 2 for x in lst if isinstance(x, int))