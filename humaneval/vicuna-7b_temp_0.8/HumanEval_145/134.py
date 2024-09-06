
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
    def _sum_digits(x):
        """Sum of digits of the given integer"""
        return sum(int(d) for d in str(x))

    def _index(x):
        """Index of the given integer in the original list"""
        return nums.index(x)

    def _sort_ascending(a, b):
        """Compare two items in ascending order"""
        return cmp(_sum_digits(a), _sum_digits(b))

    def _sort_by_points(nums):
        """Sort the given list of integers in ascending order"""
        return sorted(nums, key=_sort_ascending)

    return _sort_by_points(nums)