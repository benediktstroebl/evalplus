def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list based on the criteria.
    """
    if len(nums) == 0:
        return []
    summed_digits = []
    for num in nums:
        sum_ = 0
        for digit in str(num):
            sum_ += int(digit)
        summed_digits.append(sum_)
    sorted_nums = sorted(nums, key=lambda x: (summed_digits.index(sum_), x))
    return sorted_nums