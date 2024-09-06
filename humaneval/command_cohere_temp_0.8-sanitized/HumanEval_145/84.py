def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list of integers.
    """
    if not nums:
        return []

    # Calculate the digit-based score of each number
    def digit_score(num):
        return sum(int(d) for d in str(abs(num)))

    # Sort by digit score with a custom comparison function
    sorted_nums = sorted(nums, key=lambda x: (digit_score(x), x, nums.index(x)))

    return sorted_nums