
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
    digits = {digit: i for i, digit in enumerate(str(num))}
    sorted_nums = sorted(nums, key=lambda x: sum(digits[digit] for digit in str(x)))
    return [nums[i] for i in range(len(sorted_nums)) if i in range(len(sorted_nums))]
