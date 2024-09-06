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

    # Iterate through the list and calculate the digit-wise sum for each integer
    digit_sum_dict = {}
    for idx, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_dict:
            digit_sum_dict[digit_sum].append(idx)
        else:
            digit_sum_dict[digit_sum] = [idx]

    # Sort the indices based on the digit-wise sum and original index
    sorted_indices = sorted(digit_sum_dict.values(), key=lambda x: [x[0], -x[1]])

    # Generate the sorted list using the sorted indices
    sorted_nums = [nums[idx] for idx in sorted_indices[0]]

    return sorted_nums