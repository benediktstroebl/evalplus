
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
    # How many negative numbers are there?
    neg_count = 0
    # How many numbers are positive but less than 10?
    small_pos_count = 0
    # How many numbers are positive and greater than 10?
    large_pos_count = 0
    for num in arr:
        sign = num / 10  # negative if num is negative
        num = abs(num)  # make it positive or zero
        if num > 0:
            large_pos_count += 1
        elif num < 10:
            small_pos_count += 1
        else:
            neg_count += 1

    return neg_count + 2 * small_pos_count + large_pos_count
