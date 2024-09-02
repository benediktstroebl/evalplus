
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
    def _reduce(x):
        if not x:
            return [0]
        else:
            if not isinstance(x, int):
                return [0]
            else:
                x = x - x % 10
                if x > 0:
                    return [x] + _reduce(x // 10)
                else:
                    return _reduce(x // 10) + [10 - x % 10]

    return sorted(map(_reduce, nums), key=_reduce.getter(), reverse=True)