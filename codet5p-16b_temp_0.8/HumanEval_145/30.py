
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    import math

    digit_nums = []

    for num in nums:
        digit_nums.append(sum([int(num) for num in str(num)]))

    new_nums = sorted(nums, key=lambda x: digit_nums.index(sum([int(num) for num in str(x)]))
        if digit_nums.index(sum([int(num) for num in str(x)])) > -1
        else -1)

    return new_nums

