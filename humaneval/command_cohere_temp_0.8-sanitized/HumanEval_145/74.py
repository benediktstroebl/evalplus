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

    # List of tuples for sorting, with tiebreaker being the index in the original list
    sorted_idx = [(idx, digit_sums[idx]) for idx in range(len(nums))]

    # Sort by the sum of digits (with the tiebreaker), and then revert the sorting to get the desired order
    sorted_idx.sort(key=lambda x: x[1], reverse=False)
    sorted_idx.reverse()

    # Extract the original numbers from the sorted list of tuples
    sorted_nums = [nums[idx] for idx, _ in sorted_idx]

    return sorted_nums