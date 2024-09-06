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

    # Compute the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by score, with tiebreaker being the index
    sorted_nums = sorted(zip(digit_sums, nums), key=lambda x: (x[0], x[1][0]))

    # Remove the digit_sum scores and return the sorted list
    return [nums[0] for digit_sum, nums in sorted_nums]