def sum_squares(lst):
    """
    Compute the sum of squared numbers in the given list.
    Round each element to the upper integer value.
    Return the simple list comprehension for this
    """
    return sum(map(lambda x: (x ** 2) , lst))
lst = [1,2,3]