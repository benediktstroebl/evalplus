def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    """
    if not nums:
        return []

    num_sum = []
    for num in nums:
        sum_parts = sum(map(int, str(num)))
        num_sum.append(sum_parts)

    sorted_nums = sorted(nums, key=lambda x: [num_sum.index(x[0]), x[0]])

    return sorted_nums