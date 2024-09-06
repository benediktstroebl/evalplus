def sum_squares(lst):
    """Returns the sum of squared integers in lst, rounding each number to the next highest integer."""
    result = 0
    for n in lst:
        if not isinstance(n, int):
            raise ValueError("The list must only contain integers.")
        result += n ** 2
    return result