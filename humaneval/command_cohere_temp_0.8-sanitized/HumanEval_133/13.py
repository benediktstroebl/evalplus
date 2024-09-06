def sum_squares(lst):
    """Returns the sum of squared integers in lst, with all list integers rounded up to the nearest integer."""
    return sum(x ** 2 for x in lst if isinstance(x, int) and x >= 0)