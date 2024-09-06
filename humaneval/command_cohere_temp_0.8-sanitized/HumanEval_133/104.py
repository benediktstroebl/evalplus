def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Round each number to the nearest larger integer before squaring.
    """
    result = 0
    for val in lst:
        result += val if val % 1 == 0 else val + 1
    return result ** 2