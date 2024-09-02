
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
    def func(x, y):
        if x + y >= 0:
            return x + y
        else:
            return x - y
    nums.sort(key=lambda x: func(x[0], x[1]))
    return
