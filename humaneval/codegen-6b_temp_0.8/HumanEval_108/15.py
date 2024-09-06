
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
    zero = 0
    one = 0
    for n in arr:
        if n == 0:
            zero += 1
        elif n == 1:
            one += 1
        elif n < 0:
            n = abs(n)
            if n % 9 == 0:
                zero += 1
            else:
                one += 1
    return zero + one

