def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given integer.
    """
    sum = 0
    num = str(num)
    for digit in num:
        sum += int(digit)
    return sum
def x_index(num):
    """
    Find the index of the given integer in the original list.
    """
    index = nums.index(num)
    return index