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
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Split the list into groups with equal sums (if applicable)
    unique_digit_sum_indices = sorted(range(len(digit_sums)), key=digit_sums.count, reverse=True)
    grouped_nums = [nums[i] for i in unique_digit_sum_indices]

    # Sort each group by index in the original list
    sorted_groups = [group[:index] for group in grouped_nums for index in range(len(group))]

    return sorted(sorted_groups[0] if len(sorted_groups) == 1 else sorted_groups)