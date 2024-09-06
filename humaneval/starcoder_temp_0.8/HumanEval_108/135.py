
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    # The sum of numbers with positive sum of digits is equal to
    # the sum of numbers with negative sum of digits
    # because 1 + 2 + 3 = -1 + -2 + -3
    return count_nums_with_positive_sum_of_digits(arr) + count_nums_with_negative_sum_of_digits(arr)

