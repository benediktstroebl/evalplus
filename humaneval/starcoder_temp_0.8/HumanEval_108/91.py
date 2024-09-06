
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
    if len(arr) == 0:
        return 0
    if arr[0] < 0:
        sum1 = -1 * (abs(arr[0]))
    else:
        sum1 = arr[0]
    sum2 = 0
    for i in range(1, len(arr)):
        if arr[i] < 0:
            sum2 = -1 * (abs(arr[i]))
        else:
            sum2 = arr[i]
        if sum1 + sum2 > 0:
            sum1 += sum2
    if sum1 > 0:
        return 1
    else:
        return 0

