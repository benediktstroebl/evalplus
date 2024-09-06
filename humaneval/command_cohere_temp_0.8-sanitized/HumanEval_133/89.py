def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Round each number to the nearest larger integer first.
    """
    result = sum(int(round(n) ** 2 for n in lst))
    return result