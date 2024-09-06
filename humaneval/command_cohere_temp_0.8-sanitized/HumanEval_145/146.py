def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []
    
    num_sum = []
    for num in nums:
        sum_ = 0
        for digit in str(num):
            sum_ += int(digit)
        num_sum.append(sum_)

    sorted_nums = sorted(nums, key=lambda x: [num_sum.index(x[1]), x[1]])
    
    return sorted_nums