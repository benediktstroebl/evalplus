def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on index.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list based on the criterion

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Combine digital sums and original positions as a sorted key
    # Ex: [1, -11, 11, 4] -> [-14, -4, 10, 4]
    combined = [-sum(map(int, str(n))) for n in nums]
    combined = combined + [float('inf')] * (len(nums) - len(combined))
    sorted_nums = [nums[i] for i in range(len(nums)) if combined[i] == combined[i + 1]]

    # Sort by combined key with index-based tiebreaker
    sorted_nums = sorted(sorted_nums, key=lambda x: (x[1], x[0]))

    return sorted_nums