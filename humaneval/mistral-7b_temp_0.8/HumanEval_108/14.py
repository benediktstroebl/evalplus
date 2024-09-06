
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

    def sum_digits(n):
        if n < 0:
            n = -n
        d = 0
        while n != 0:
            d += n % 10
            n = n // 10
        return d

    nums = 0
    for x in arr:
        nums += 1 if sum_digits(x) > 0 else 0
    return nums
