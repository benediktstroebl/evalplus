def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers with no guaranteed order.

    Returns:
        list: Ordered list according to criteria above.
    """
    if not nums:
        return []

    # Track the sorted list in descending order by sum of digits and original index.
    sorted_idx = sorted(range(len(nums)), key=lambda idx: (len(str(nums[idx])) - sum(int(d) for d in str(nums[idx])), idx))
    # Reverse the order to sort in ascending order.
    return [nums[i] for i in sorted_idx[::-1]]