def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    # Empty list handling
    if not nums:
        return []

    # Convert list to set to avoid index issues
    # (consider numbers like 2017 which has the same digit sum)
    digits = {sum(map(int, str(num))) for num in nums}
    sorted_digits = sorted(digits)
    sorted_nums = [nums[i] for i in range(len(nums)) if sum(map(int, str(nums[i]))) in sorted_digits]
    return sorted_nums