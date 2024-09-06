def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of digits of the given integer.

    Args:
        num (int): Integer for which the sum of digits needs to be calculated.

    Returns:
        int: Sum of digits of the given integer.
    """
    sum_so_far = 0
    num = str(num)
    for digit in num:
        sum_so_far += int(digit)
    return sum_so_far
def x_index(num):
    """
    Determine the index of the given integer in the original list.

    Args:
        num (int): Integer for which the index needs to be determined.

    Returns:
        int: Index of the given integer in the original list.
    """
    return nums.index(num) if num in nums else -1