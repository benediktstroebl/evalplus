def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum of digits for each number
    DigitSum = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by digit sum, then by original index in case of ties
    sorted_idx = sorted(range(len(nums)), key=lambda i: (DigitSum[i], i))

    return [nums[i] for i in sorted_idx]