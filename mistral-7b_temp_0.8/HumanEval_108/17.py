
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
    s = 0
    for x in arr:
        if x < 0:
            s += x // 10
        else:
            s += x % 10
    return s
    return sum(1 for x in arr if sum(int(d) for d in str(x)) > 0)
    return sum(map(lambda x: 1 if sum(int(d) for d in str(x)) > 0 else 0, arr))

