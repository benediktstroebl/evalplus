def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on criteria above.
    """
    if len(nums) == 0:
        return []

    # Explicitly defining the return type as an iterable to allow sorting
    return sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))