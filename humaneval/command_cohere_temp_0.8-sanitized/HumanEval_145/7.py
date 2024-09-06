def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if len(nums) == 0:
        return []

    summed_digits = [sum(map(int, str(num))) for num in nums]
    indexed_nums = list(zip(nums, summed_digits))
    
    sorted_nums = sorted(indexed_nums, key=lambda x: (x[1], x[0]))
    return [num for num, _ in sorted_nums]