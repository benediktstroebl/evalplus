def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sorting of the input list according to the specified criteria.
    """
    if not nums:
        return []

    def sum_digits(num):
        return sum(int(d) for d in str(num))

    sorted_nums = sorted(nums, key=lambda x: (sum_digits(x), x))
    return sorted_nums