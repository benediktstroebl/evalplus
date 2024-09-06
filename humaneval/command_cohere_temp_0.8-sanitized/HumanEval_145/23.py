def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list based on the criteria specified.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Organize criteria based on sum of digits and original index
    ordered = [(sum(map(int, str(n))), i) for i, n in enumerate(nums)]

    # Sort based on criteria and convert back to integer list
    return [n for _, n in sorted(ordered)]