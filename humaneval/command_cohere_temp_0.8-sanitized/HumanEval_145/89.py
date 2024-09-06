def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the digit in the original list.

    Args:
        nums (List[int]): List of integers to be sorted.

    Returns:
        List[int]: Ordered list according to the criteria.
    """
    if not nums:
        return []

    # Track the sorted order in ascending order based on sum of digits and original index.
    # We use a list to preserve the original order in case of ties.
    sorted_order = []
    digit_sum_to_index = {}  # Dictionary for quick look-up of original index based on digit sum.

    for index, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_to_index:
            sorted_order.append(nums[digit_sum_to_index[digit_sum]])
            digit_sum_to_index[digit_sum] = index
        else:
            sorted_order.append(num)
            digit_sum_to_index[digit_sum] = index

    return sorted_order