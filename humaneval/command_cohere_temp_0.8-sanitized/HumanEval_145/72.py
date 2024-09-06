def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list based on criteria.
    """
    if not nums:
        return []

    sorted_nums = [num for ind, num in enumerate(nums) if ind == nums.index(num)]
    sorted_nums = [num for num in sorted_nums if num != 0]
    
    return sorted_nums