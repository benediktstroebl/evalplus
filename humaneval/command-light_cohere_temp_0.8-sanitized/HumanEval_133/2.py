def sum_squares(lst):
    """
    Computes the sum of squared numbers in the given list.

    Parameters:
    lst (list): list of numbers

    Returns:
        float: sum of the squared numbers
    """
    # Compute the sum of the squares of numbers
    s = 0
    for i in lst:
        s += i * i
    return s