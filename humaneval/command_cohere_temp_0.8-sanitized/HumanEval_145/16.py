def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    # Copy the list to avoid modifying the original
    nums = nums[:]
    # Sort by digit sum, using the tiebreaker logic
    nums.sort(key=lambda x: (sum(int(d) for d in str(x)), x))
    return nums