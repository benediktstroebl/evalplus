
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
    if not arr:
        return 0
    n = len(arr)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            num = arr[i] + arr[j]
            if num > 0:
                res += 1
                break
        else:
            res += 1
    return res
    