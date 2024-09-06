def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers with no explicit upper bound.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    # Make copies of the lists to avoid modifying the original list.
    nums_copy = nums.copy()
    digit_sums = [sum(int(d) for d in str(n)) for n in nums_copy]
    index_sorts = [nums.index(n) for n in nums_copy]

    # Sort by sum of digits with tiebreaks.
    sorted_idx = sorted(range(len(nums)), key=lambda i: [digit_sums[i], index_sorts[i]])

    return [nums_copy[idx] for idx in sorted_idx]