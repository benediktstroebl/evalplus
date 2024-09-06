def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria specified.
    """
    if len(nums) == 0:
        return []

    # Calculate the digit-sum-sorted order without tie breaks, i.e. a possible base solution.
    digit_sums = [sum(map(int, str(n))) for n in nums]
    digit_sorted = [nums[i] for i in reversed(sorted(list(enumerate(digit_sums)), key=lambda x: x[1]))]

    # Iterate through the list and locate the positions of elements in the original list
    # in the digit-sum-sorted list to determine the final order with tie breaks applied.
    final_order = []
    curr_index = 0
    for n in nums:
        while digit_sorted[curr_index] != n:
            curr_index += 1
        final_order.append(n)
        curr_index += 1

    return final_order