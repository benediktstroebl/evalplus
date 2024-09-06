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

    # Calculate the total digit sum for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by digit sum (default sorting method)
    sorted_by_digit_sum = sorted(zip(digit_sums, nums), key=lambda x: x[0])

    # Now reconstruct the sorted list and return it
    return [n for digit_sum, n in sorted_by_digit_sum]