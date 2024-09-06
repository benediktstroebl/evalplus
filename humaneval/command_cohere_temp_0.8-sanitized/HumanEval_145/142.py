def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Convert negative numbers to positive for the digit sum comparison
    positive_nums = [num for num in nums if num >= 0]
    negative_nums = [-num for num in nums if num < 0]
    combined_nums = positive_nums + negative_nums

    # Sort by digit sum with tiebreaks
    sorted_digits = sorted(combined_nums, key=lambda x: (sum(map(int, str(x))), x))

    # Reconstruct the sorted list without negative numbers
    sorted_result = [x for x in sorted_digits if x >= 0]

    return sorted_result