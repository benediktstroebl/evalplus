
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
    sum_digits = 0
    num_elements = 0
    for x in arr:
        while x > 0:
            if x % 10 > 0:
                sum_digits += 1
            x //= 10
        x = 0
        num_elements += 1
    return sum_digits
