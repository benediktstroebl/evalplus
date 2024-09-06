def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    # Helper function to calculate the sum of digits for an integer
    def sum_of_digits(num):
        return sum(int(d) for d in str(num))

    # Sort the list based on the sum of digits with a tiebreaker mechanism
    return sorted(nums, key=lambda num: (sum_of_digits(num), nums.index(num)))