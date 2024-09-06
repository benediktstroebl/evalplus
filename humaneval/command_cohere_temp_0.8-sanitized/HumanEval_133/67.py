def sum_squares(lst):
    """
    Return the sum of squared integers in the list, with each list item being rounded up to the nearest integer.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of the squared integers.
    """
    return sum(x * x for x in lst if isinstance(x, int) and x >= 0)