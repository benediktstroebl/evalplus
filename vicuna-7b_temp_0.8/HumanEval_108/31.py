
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
    digits = [x - sum(d < 0 for d in str(n)) for n in arr]
    positive_sums = [sum(d > 0 for d in str(n)) for n in arr]
    return len(digits) - len(set(positive_sums))