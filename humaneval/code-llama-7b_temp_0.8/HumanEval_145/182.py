
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
    from collections import defaultdict
    num_to_points = defaultdict(int)
    nums_with_points = []
    for num in nums:
        num_points = sum(int(n) for n in str(num))
        num_to_points[num] = num_points
    nums_with_points = sorted(nums, key=num_to_points.get)
    return nums_with_points

