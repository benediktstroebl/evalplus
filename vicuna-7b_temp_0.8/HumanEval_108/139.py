
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
    # Check for empty list
    if not arr:
        return 0
    # Check for negative numbers
    for num in arr:
        if num < 0:
            neg_sum = abs(sum(map(int, num)))
            sign = -1
        else:
            neg_sum = 0
            sign = 1
    # Sum of digits
    sum_digits = 0
    # Iterate over list
    for num in arr:
        num_digits = sum(map(int, num))
        sign_num = sign * num_digits
        sum_digits += sign_num
    # Return number of elements with positive sum of digits
    return sum_digits > 0