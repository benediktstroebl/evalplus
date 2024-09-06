def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Compute the sum-of-digits score for each number and sort them accordingly.
    sorted_nums = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))

    # However, the original list's order should take precedence in case of identical sums.
    return [sorted_nums[i] for i in range(len(sorted_nums))]