def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True

    Returns:
        List: Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        (int) num: Number whose digit sum needs to be calculated.

    Returns:
        int: Sum of digits of the given number.
    """
    return sum(int(digit) for digit in str(num))
def x_index(num):
    """
    Identify the index of the given number in the original list.

    Args:
        (int) num: Number whose index needs to be determined.

    Returns:
        int: Index of the number in the original list.
    """
    return nums.index(num) if nums.count(num) == 1 else -1