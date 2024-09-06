
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
    sum_of_digits = 0
    num_of_digits = 0
    for item in arr:
        while item > 0:
            digit = item % 10
            item = item // 10
            sum_of_digits += digit
            num_of_digits += 1
        if sum_of_digits > 0:
            yield True
        sum_of_digits = 0
        num_of_digits = 0

