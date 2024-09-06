
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

    # Sorting by points
    def point_sum(x):
        return sum([int(x) for x in str(x)])

    # Sorting by index
    def index_sum(x):
        return sum([x.index(y) for y in nums])

    return sorted(nums, key=lambda x: (point_sum(x), index_sum(x)))
