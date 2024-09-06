def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the integer in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Copy the list to prevent original list modification
    nums = nums[:]
    nums.sort(key=lambda x: (sum_of_digits(x), x_index(x)))
    return nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given integer.
    """
    return sum(int(d) for d in str(num))
def x_index(num):
    """
    Find the index of the given integer in the original list.
    """
    return nums.index(num) if nums.count(num) == 1 else -1