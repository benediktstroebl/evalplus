
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

    def digit_sum(x):
        if x < 0:
            x = -x
        ans = 0
        while x:
            ans += x % 10
            x //= 10
        return ans
    return sorted(nums, key=lambda x: (digit_sum(x), x))
