def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers with no guaranteed order.

    Returns:
        list: Ordered list according to the specified criteria.
    """
    if not nums:
        return []

    # Calculate the digit-sum-ordered index for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
    digit_idx = [digit_sums.index(ds) for ds in digit_sums]

    # Base case: If there are no ties, return the list in the calculated order
    if len(set(digit_idx)) == len(digit_idx):
        return nums[digit_idx]

    # If there are ties, use the index in the original list as a tie breaker
    ordered_nums = []
    for i in range(len(nums)):
        if digit_idx[i] == digit_idx[:i+1].count(digit_idx[i]):
            ordered_nums.append(nums[i])

    return ordered_nums