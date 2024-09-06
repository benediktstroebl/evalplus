
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
    def has_positive_sum(num):
        if num < 0:
            num = -num
        return 1 if num == 0 else num % 10 + has_positive_sum(num // 10)
    return len(list(filter(has_positive_sum, arr)))

