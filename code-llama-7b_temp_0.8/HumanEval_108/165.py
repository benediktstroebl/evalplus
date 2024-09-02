
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
    if len(arr) == 0:
        return 0
    positive_nums = [num for num in arr if num > 0]
    negative_nums = [num for num in arr if num < 0]
    negative_nums_sum = 0
    positive_nums_sum = 0
    negative_nums_len = len(negative_nums)
    positive_nums_len = len(positive_nums)
    for num in negative_nums:
        negative_nums_sum += sum_num(num)
    for num in positive_nums:
        positive_nums_sum += sum_num(num)
    if negative_nums_sum > 0:
        return positive_nums_len + negative_nums_len
    else:
        return positive_nums_len
