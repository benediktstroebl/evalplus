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

    # Initialize the list to store sorted numbers based on digit sum and original index.
    sorted_nums = [(-num, i) for i, num in enumerate(nums)]

    # Sort the list according to the calculated key.
    sorted_nums.sort()

    # Extract just the sorted numbers, without the original indices.
    return [num for _, num in sorted_nums]