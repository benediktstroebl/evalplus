def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next highest integer.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of squared integers.
    """

    # Ensure all list elements are integers (with rounding)
    lst = [int(x + 1) for x in lst]

    # Calculate the sum of squares
    result = sum(x ** 2 for x in lst)

    return result