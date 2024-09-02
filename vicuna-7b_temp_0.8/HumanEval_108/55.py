
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
    arr = list(arr)
    if not arr:
        return 0
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            digit1 = arr[i] * 10 + arr[j]
            count += digit1 if digit1 > 0 else -count - 1
    return count