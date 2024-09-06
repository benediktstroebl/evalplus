
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
    # keep track of the numbers which have been checked
    seen = {}
    # keep track of the numbers which have more than 0 digits,
    # and are positive
    more_than_zero_nums = 0

    for num in arr:
        num_str = str(num)
        if num_str in seen:
            continue
        # check if num is negative, and if the first digit is negative
        is_negative = num < 0
        first_digit = get_first_digit(num)
        if is_negative and first_digit < 0:
            continue

        # add to the number of numbers with more than 0 digits
        if len(num_str) > 0:
            more_than_zero_nums += 1

        # add the number to the seen dict
        seen[num_str] = 1

    return more_than_zero_nums
