
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
    num_points = collections.defaultdict(int)
    for num in nums:
        num_points[sum_of_digits(num)] += 1
    return [num for num, count in num_points.items() if count > 0]
