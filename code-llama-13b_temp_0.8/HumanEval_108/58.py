
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
    result = 0
    for i in arr:
        digit_sum = 0
        if i < 0:
            i = abs(i)
            digit_sum = -1
        while i > 0:
            digit_sum += i % 10
            i = i // 10
        if digit_sum > 0:
            result += 1
    return result

