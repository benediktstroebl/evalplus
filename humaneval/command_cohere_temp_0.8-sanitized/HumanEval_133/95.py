def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest upper int first.
    """
    result = sum(int(rounding(n)) ** 2 for n in lst for rounding in (lambda x: x, lambda x: x + 0.5, lambda x: x - 0.5) if int(rounding(n)) ** 2)
    return result