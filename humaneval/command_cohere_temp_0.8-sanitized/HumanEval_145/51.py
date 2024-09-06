def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Split the list into sorted groups according to digit_sums
    sorted_groups = [nums[idx:] for idx in range(len(nums)) if digit_sums[idx] >= digit_sums[idx+1]]

    # Sort each group according to index in the original list
    sorted_groups = [group[idx:] for group in sorted_groups for idx in range(len(group))]

    return sorted_groups[0]