def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list based on the criteria.
    """
    if not nums:
        return []

    sorted_nums = [num for ind, num in enumerate(nums) if summ_digits(num) == summ_digits(nums[0]) and ind == 0]
    sorted_nums.extend([num for num in nums if summ_digits(num) < summ_digits(nums[0])])
    sorted_nums.extend([num for ind, num in enumerate(nums) if summ_digits(num) == summ_digits(nums[0]) and ind > 0])
    return sorted_nums
def summ_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number for which the digit sum is calculated.

    Returns:
        int: Sum of the digits of the given number.
    """
    return sum(int(d) for d in str(num))