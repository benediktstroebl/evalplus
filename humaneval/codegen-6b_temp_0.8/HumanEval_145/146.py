
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
    from functools import cmp_to_key
    return sorted(nums, key=cmp_to_key(lambda x, y: sum(int(c) for c in str(x) + str(y)) - sum(int(c) for c in str(y) + str(x))))

