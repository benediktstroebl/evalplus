def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True

    Args:
        nums: List of integers to be sorted.
    Returns:
        sorted_nums: Sorted list based on criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
    return sorted_nums