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

    # Calculate the total digit sum for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # List of tuples for sorting: (digit_sum, original_index)
    sorted_idx = [(ds, i) for i, (ds, n) in enumerate(zip(digit_sums, nums))]

    # Sort by digit sum, then by index as a tiebreaker
    sorted_idx.sort(key=lambda x: (x[0], x[1]))

    return [n for ds, i in sorted_idx for n in nums[i:]]