def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list according to criteria above
    """
    if not nums:
        return []
    summed_digits = []
    for num in nums:
        sum_ = 0
        for digit in str(num):
            sum_ += int(digit)
        summed_digits.append(sum_)
    sorted_nums = sorted(nums, key=lambda x: (summed_digits.index(sum_), x))
    return sorted_nums