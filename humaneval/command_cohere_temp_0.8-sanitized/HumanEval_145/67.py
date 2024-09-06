def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    # Extract the digit sum for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by digit sum, and then by original index for ties
    return sorted(nums, key=lambda x:[digit_sums.index(sum(int(d) for d in str(x))), x])