
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
    # list comprehension
    # return sorted(nums, key=lambda x: sum([int(i) for i in str(abs(x))]))
    # map + lambda
    # return sorted(nums, key=lambda x: sum(map(lambda x: int(x), str(abs(x)))))
    # sort + lambda
    # return sorted(nums, key=lambda x: sum(map(lambda x: int(x), str(abs(x)))))

    # 1 line
    return sorted(nums, key=lambda x: sum([int(i) for i in str(abs(x))]))

