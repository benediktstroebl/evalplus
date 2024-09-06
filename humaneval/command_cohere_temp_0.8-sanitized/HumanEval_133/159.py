def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest upper int first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result