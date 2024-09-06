def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    # Calculate the sum-of-digits for each number
    sod = [sum(int(d) for d in str(num)) for num in nums]

    # Initially sort by sum-of-digits with tiebreaker on index
    sorted_nums = sorted(zip(nums, sod), key=lambda x: (x[1], x[0][0]))
    return [num for num, _ in sorted_nums]