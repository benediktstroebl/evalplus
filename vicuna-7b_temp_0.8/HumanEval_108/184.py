
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
    n = len(arr)
    if n == 0:
        return 0
    sum_pos = 0
    for i in range(n):
        if arr[i] >= 0:
            sum_pos += arr[i]
        else:
            sum_neg = abs(arr[i])
            sum_pos += sum_neg // 10
            sum_neg %= 10
    return sum_pos
