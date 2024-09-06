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

    # Calculate the sum of digits for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by digit sums (with indexing as tiebreaker)
    sorted_idx = sorted(range(len(nums)), key=lambda i: (digit_sums[i], i))

    # Reconstruct the sorted list
    return [nums[idx] for idx in sorted_idx]