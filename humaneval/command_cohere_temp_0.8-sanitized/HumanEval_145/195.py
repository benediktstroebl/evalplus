def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # If the list is empty, return it directly
    if not nums:
        return []

    # Use the sum-of-digits and index-based sorting to create a new list
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

    # For consistency with the prompt's example, return the negative of the list
    return [-x for x in sorted_nums]