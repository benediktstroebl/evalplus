def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list according to criteria above
    """
    if len(nums) == 0:
        return []

    # Keep track of the items with the highest digit sum at each index
    items_at_index = [-1] * len(nums)

    # Sort criteria based on sum of digits and original index
    sorted_nums = sorted(nums, key=lambda x: [x[0] for _ in range(10) if x != -x][0] + [nums.index(x)])

    # Use the original index as a tie-breaker to get the desired ordering
    sorted_nums = [sorted_nums[i] for i in items_at_index]

    return sorted_nums