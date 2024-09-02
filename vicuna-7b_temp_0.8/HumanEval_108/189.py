
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
    count = 0
    for num in arr:
        sign = -1 if num < 0 else 1
        digs = [d if d > 0 else 0 for d in str(num)]
        if len(digs) > 0:
            count += len(digits)
    return count
