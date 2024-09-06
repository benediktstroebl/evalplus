def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each list element to the nearest integer.
    """
    result = sum(int(round(n)) ** 2 for n in lst)
    return result