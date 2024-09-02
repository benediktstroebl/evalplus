
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
    nums_by_points = [num for num in nums if sum(map(int, str(num))) >= 0]
    points = {num: sum(map(int, str(num))) for num in nums_by_points}
    points = dict(sorted(points.items(), key=lambda item: item[1]))

    return [
        num
        for num in nums
        if num not in nums_by_points
    ] + list(points.keys())
