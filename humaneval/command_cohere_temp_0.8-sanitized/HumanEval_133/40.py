def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each list element to the nearest larger integer.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of squared integers in the list.
    """

    # Convert the list to a set to remove duplicates
    integers = set(x for x in lst if x % 1 == 0)

    return sum(x ** 2 for x in integers)