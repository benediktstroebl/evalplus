def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list based on the criteria above.
    """
    if not nums:
        return []

    # Calculate the sum-of-digits histogram
    histogram = [0] * 10
    for num in nums:
        histogram[sum(str(num)) % 10] += 1

    # Build the sorting order based on the histogram and original index
    sorting_order = [i for i in range(len(nums))]
    for i in range(1, 10):
        sorting_order[histogram[i] :: -1] = i

    # Sort the original list based on the sorting order
    ordered_nums = [nums[i] for i in sorting_order]

    return ordered_nums