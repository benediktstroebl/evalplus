
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

    if len(nums) == 0:
        return []

    def sum_digits(n):
        return sum(map(lambda c: int(c), list(str(n))))

    nums_with_points = [(n, sum_digits(n)) for n in nums]
    return sorted(nums_with_points, key=lambda pair: (pair[1], pair[0]))
