
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
    # NOTE: This solution uses a dictionary to keep track of the number of
    # positive and negative numbers that sum to a given number.
    # This approach allows the function to efficiently determine the
    # number of positive and negative numbers that sum to a given number.

    sum_digits = 0
    num_pos = 0
    num_neg = 0
    for num in arr:
        digit = abs(num)
        if digit > 0:
            num_pos += 1
            sum_digits += digit
        else:
            num_neg += 1
            sum_digits += digit
    return num_pos, num_neg
