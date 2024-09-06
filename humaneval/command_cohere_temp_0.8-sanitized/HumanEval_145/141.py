def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    """
    if not nums:
        return []

    num_counts = [sum(map(int, str(n))) for n in nums]
    idx_counts = [tuple(str(n).count('0') for n in str(i)) for i in range(len(nums))]

    # Sort by digit sum with tiebreaker
    sorted_idx = sorted(range(len(nums)), key=lambda k: (num_counts[k], idx_counts[k]))

    return [nums[i] for i in sorted_idx]