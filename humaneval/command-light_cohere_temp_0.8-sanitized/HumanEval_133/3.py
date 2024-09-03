def sum_squares(lst):
    """
    Compute the sum of squared numbers in the given list,
    round each element in the list to the upper integer(Ceiling) first.

    Args:
        lst (list) -> list of numbers

    Returns:
        int
    """
    return sum(map(lambda x: (x ** 2 + 1) ** .5, lst))