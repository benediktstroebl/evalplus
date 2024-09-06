def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Split the list into tiers based on digit sum
    tier_groups = [nums[idx:next_idx] for idx, next_idx in enumerate(
        range(0, len(digit_sums), 1))
                    if digit_sums[idx:] == digit_sums[idx:next_idx]]

    # Sort each tier separately with the tiebreaker being the index
    sorted_nums = [tier for tier in tier_groups if tier]
    for i in range(len(sorted_nums)):
        tier = sorted_nums[i]
        # If there's a tie, sort by the index of the first element
        tier.sort(key=lambda x: (x, tier.index(x)))

    return sorted_nums[0] if sorted_nums else []