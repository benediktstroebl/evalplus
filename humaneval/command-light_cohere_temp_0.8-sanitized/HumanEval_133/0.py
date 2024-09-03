def sum_squares(lst):
    """
    Calculate the sum of squared numbers in the given list,
    round each element to the upper int(Ceiling) first.
    Return the sum of the squared numbers.
    Examples:
    For lst = [1,2,3] return 14
    For lst = [1,4,9] return 98
    For lst = [1,3,5,7] return 84
    For lst = [1.4,4,0] return 2880
    """

    # Test cases
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([1, 4, 9]) == 98
    assert sum_squares([1, 3, 5, 7]) == 84
    assert sum_squares([1.4, 4, 0]) == 2880
    assert sum_squares([-2, 4, 1, 1]) == 6

    return sum_squares