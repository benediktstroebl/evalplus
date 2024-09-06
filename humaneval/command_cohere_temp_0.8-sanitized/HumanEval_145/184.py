def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Sorting of the input list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Calculate the sum_map which holds the sum of digits for each number
    sum_map = {num: sum(int(d) for d in str(num)) for num in nums}

    # Sort the numbers based on the sum of their digits with tiebreak by index
    sorted_nums = sorted(nums, key=lambda num: [sum_map[num], nums.index(num)])

    return sorted_nums