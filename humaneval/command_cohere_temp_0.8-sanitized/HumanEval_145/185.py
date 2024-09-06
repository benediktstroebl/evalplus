def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Split the list into lists according to digit sums
    grouped = [nums[i:j] for i, j in zip(range(0, len(digit_sums)), iter(enumerate(digit_sums)))]

    # Sort the sublists by element index
    sorted_groups = [group[idx] for group, (idx, _) in zip(grouped, sorted(enumerate(digit_sums), key=lambda x: x[1]))]

    return sorted(sorted_groups[0]) + sorted_groups[1:]