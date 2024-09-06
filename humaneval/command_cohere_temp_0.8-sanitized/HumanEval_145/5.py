def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sorteed list based on criteria.
    """
    if len(nums) == 0:
        return []
    sorted_nums = [num for ind, num in enumerate(nums) if ind != nums.index(num)]
    # Manually implementing sorting with respect to the index and digit sum.
    for ind in range(len(nums)):
        digit_sum = sum([int(d) for d in str(nums[ind]) if d.isdigit()])
        sorted_nums.append(nums[ind])
        prev_ind = nums[digit_sum].index(nums[ind])
        if prev_ind > ind:
            # Swap to maintain original index order among digit sum ties.
            sorted_nums[ind], sorted_nums[prev_ind] = sorted_nums[prev_ind], sorted_nums[ind]
    return sorted_nums