def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list based on the criteria above.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums