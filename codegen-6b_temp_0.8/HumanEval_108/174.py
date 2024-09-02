
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
    count = 0
    for e in arr:
        if e > 0:
            count += 1
        if e < 0:
            count += 1
            first_digit = e // -10
            if first_digit < 0:
                first_digit *= -1
            count += first_digit
    return count
