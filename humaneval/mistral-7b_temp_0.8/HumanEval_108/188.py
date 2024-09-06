
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
    n_nums = 0
    for i in arr:
        digit_sum = 0
        i = abs(i)
        while i > 0:
            digit = i%10
            digit_sum += digit
            i //= 10
        if digit_sum > 0:
            n_nums += 1
    return n_nums
