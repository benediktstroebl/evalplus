
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

    def _count_nums(arr, i=0):
        if i == len(arr):
            return 0
        elif _sum_of_digits(arr[i]) > 0:
            return 1 + _count_nums(arr, i + 1)
        else:
            return _count_nums(arr, i + 1)

    return _count_nums(arr)

