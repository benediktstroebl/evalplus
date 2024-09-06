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

    sorted_nums = [num for ind, num in enumerate(nums) if ind != nums.index(num)]

    for num in nums:
        digit_sum = sum(int(d) for d in str(num))
        index = nums.index(num)
        sorted_nums.append(num for num in nums if (digit_sum, index) == (sorted_nums[-1:][0], sorted_nums[-1:][1]))

    return sorted_nums