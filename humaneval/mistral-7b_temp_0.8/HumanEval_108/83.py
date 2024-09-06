
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

    # DON'T CHANGE CODE BELOW ðŸ‘‡
    # a = arr
    a = arr
    b = 0
    c = 0
    for n in a:
        if n < 0:
            c = -1
            n = n * (-1)
        if n > 0:
            c = 1
        b = b + c

    # DON'T CHANGE CODE ABOVE ðŸ‘†
    return b

