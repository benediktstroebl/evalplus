def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sorteed list based on the criteria.
    """
    if len(nums) == 0:
        return []

    # Keep track of the sorted list based on digit sum.
    sorted_by_sum = []

    # Keep track of the original index for tiebreaking.
    original_index_tracker = [-1] * len(nums)

    for digit_sum in range(0, int(np.max(nums) + 1)):
        # Find all elements in the list that have this digit sum.
        current_group = [num for num in nums if sum(map(int, str(num))) == digit_sum]

        # Sort the group based on the original index.
        for i in range(len(current_group)):
            current_group[i] = (current_group[i], i)

        # Add the sorted group to our running result.
        sorted_by_sum.extend(current_group)

    return [num[0] for num in sorted_by_sum if num[1] > original_index_tracker[num[0]]]