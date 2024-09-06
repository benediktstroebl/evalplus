def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list based on the criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number for which the digit sum is calculated.

    Returns:
        int: Sum of the digits of the given number.
    """
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum
def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for which the index is determined.

    Returns:
        int: Index of the number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1