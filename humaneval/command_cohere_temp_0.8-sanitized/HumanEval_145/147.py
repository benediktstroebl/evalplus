def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to criteria above.
    """
    if not nums:
        return []

    def sum_of_digits(num):
        # Calculate sum of digits for a given number
        return sum(map(int, str(num)))

    # Sort the list based on sum of digits with tiebreak by index
    return sorted(nums, key=lambda x:[sum_of_digits(x), nums.index(x)])