def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the digit in the original list.

    Examples:
    - order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    - order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
    sorted_indices = sorted(range(len(nums)), key=lambda i: digit_sums[i], reverse=True)

    # Construct the sorted list based on the sorted indices.
    sorted_nums = [nums[i] for i in sorted_indices]
    return sorted_nums