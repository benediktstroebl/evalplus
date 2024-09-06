def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Track the indices of elements with equal sums of digits for tiebreaking.
    digit_sum_indices = []

    # Traverse the list and maintain the mapping of digit sums to indices.
    for i, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        digit_sum_indices.append((digit_sum, i))

    # Sort the list based on the calculated digit sums and their original indices.
    sorted_nums = sorted(nums, key=lambda num: (digit_sum_indices.index(tuple(el) for el in zip(*sorted((digit_sum, i), reverse=True)))), reverse=False)
    return sorted_nums