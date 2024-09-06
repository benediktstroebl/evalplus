def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    summed_digits = []
    original_indices = [i for i, n in enumerate(nums)]

    for n in nums:
        summed = sum(map(int, str(n)))
        summed_digits.append(summed)

    sorted_nums = sorted(zip(summed_digits, original_indices), key=lambda x: x[0], reverse=False)
    return [n for idx, n in sorted_nums]