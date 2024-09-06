def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    sorted_nums = []
    digit_sum_dict = {}

    for idx, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_dict:
            if idx < digit_sum_dict[digit_sum]:
                continue
            else:
                temp = nums[digit_sum_dict[digit_sum]]
                nums[digit_sum_dict[digit_sum]] = num
                nums[idx] = temp
        digit_sum_dict[digit_sum] = idx
        sorted_nums.append(num)

    return sorted_nums