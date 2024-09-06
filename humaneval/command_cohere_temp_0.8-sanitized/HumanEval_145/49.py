def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if len(nums) == 0:
        return []

    sorted_nums = []
    digit_sum_dict = {}

    for idx, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_dict:
            if idx < digit_sum_dict[digit_sum]:
                continue
            elif idx > digit_sum_dict[digit_sum]:
                sorted_nums.extend(nums[:digit_sum_dict[digit_sum]]);
                sorted_nums.append(num);
                sorted_nums.extend(nums[digit_sum_dict[digit_sum]:idx+1])
                digit_sum_dict[digit_sum] = idx
                continue
        sorted_nums.append(num)
        digit_sum_dict[digit_sum] = idx

    return sorted_nums