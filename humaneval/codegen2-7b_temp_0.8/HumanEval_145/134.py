
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
    nums_length = len(nums)
    if nums_length == 0:
        return []
    elif nums_length == 1:
        return nums
    else:
        sorted_nums = sorted(nums)
        return order_by_points(sorted_nums[:nums_length - 1]) + sorted_nums[nums_length - 1]

