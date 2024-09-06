def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest upper int first.
    """
    result = sum(int(rounding(num)) ** 2 for num in lst for rounding in (lambda x: x, lambda x: x + 0.5, lambda x: x - 0.5) if int(rounding(num)) ** 2)
    return result