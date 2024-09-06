def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each list element to the nearest larger integer.
    """
    result = 0
    for num in lst:
        result += num ** 2
    
    return int(result)