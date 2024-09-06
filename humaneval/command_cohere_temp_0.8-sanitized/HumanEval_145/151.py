def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list based on the criteria specified.
    """
    if not nums:
        return []
    summed_nums = [sum(map(int, str(num))) for num in nums]
    sorted_nums = sorted(zip(range(len(nums)), summed_nums), key=lambda x: x[1])
    return [num for i, num in sorted_nums]