
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
    n = len(nums)
    result = [0] * n
    for i in range(n):
        digit = sum(map(int, str(nums[i])))
        if i != 0:
            result[i] = digit - 10 * result[i - 1]
    return [nums[i] for i in range(n)]
