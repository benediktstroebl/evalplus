def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on criteria.
    """
    if not nums:
        return []

    sorted_nums = [num for ind, num in enumerate(nums) if summ_digits(num) <= summ_digits(nums[-1]) or (summ_digits(num) == summ_digits(nums[-1])) and ind < len(nums) - 1]
    
    for num in nums:
        if summ_digits(num) < summ_digits(sorted_nums[0]):
            sorted_nums = [num] + sorted_nums
        elif summ_digits(num) == summ_digits(sorted_nums[0]):
            # Check if the current number has lower index than the first element in the sorted list
            if num < sorted_nums[0] and summ_digits(num) == summ_digits(sorted_nums[0]):
                sorted_nums = [num] + sorted_nums
    
    return sorted_nums
def summ_digits(num):
    """
    Calculates the sum of digits of the given number.
    """
    if num == 0:
        return 0
    else:
        return sum(int(digit) for digit in str(num))