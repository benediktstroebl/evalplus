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

    sorted_nums = [num for ind, num in enumerate(nums) if summ_digits(num) <= summ_digits(nums[-1]) or (summ_digits(num) == summ_digits(nums[-1])) and ind == len(nums) - 1]

    for num in nums:
        if summ_digits(num) < summ_digits(sorted_nums[0]):
            sorted_nums =name_sorted(num, sorted_nums)

    return sorted_nums
def summ_digits(num):
    """
    Calculate the sum of the digits of the given number.
    """
    return sum(int(digit) for digit in str(num))
def name_sorted(num, sorted_nums):
    """
    Helper function to sort the list of integers according to the sum of their digits.
    """
    return sorted_nums.index(num)