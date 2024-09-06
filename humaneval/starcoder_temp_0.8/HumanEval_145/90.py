
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
    assert isinstance(nums, list), "argument should be a list"

    def count_digits(x):
        x = abs(x)
        return 0 if x == 0 else count_digits(x // 10) + 1

    digits = []
    for num in nums:
        digits.append([count_digits(num), num])
    digits.sort()

    nums = [d[1] for d in digits]
    return nums
