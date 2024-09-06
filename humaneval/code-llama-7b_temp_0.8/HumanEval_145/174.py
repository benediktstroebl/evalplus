
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
    nums_with_points = [(sum(int(x) for x in str(num)), nums.index(num), num) for num in nums]
    nums_with_points.sort(key=lambda x: x[0])
    return [x[2] for x in nums_with_points]
