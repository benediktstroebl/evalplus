def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list of integers.
    """
    if len(nums) == 0:
        return []

    # Make a copy of the list to preserve the original order.
    nums_copy = list(nums)

    # Sort the copy based on sum of digits and original index.
    nums_copy.sort(key=lambda x: (sum(int(d) for d in str(x)), nums.index(x)))

    return nums_copy