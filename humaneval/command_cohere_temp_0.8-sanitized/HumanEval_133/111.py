def sum_squares(lst):
    """Returns the sum of squared numbers in the list."""
    result = 0
    for n in lst:
        result += n**2

    return result