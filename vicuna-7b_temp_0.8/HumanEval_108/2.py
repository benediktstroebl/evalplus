
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
    arr = [int(x) for x in arr]
    n = 0
    for x in arr:
        if x >= 0:
            n += 1
        else:
            n += int(x) + (1 if abs(x) > 1 else 0)
    return n
