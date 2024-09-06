def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on indices.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Organize data into a format that allows quick sorting
    # By summing digits and maintaining the original index,
    # Then sorting based on the summed digit values
    sorted_nums = [(sum(map(int, str(n))), i) for i, n in enumerate(nums)]
    sorted_nums.sort()
    return [n for i, n in sorted_nums]