def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Split the list into sorted groups according to the digit-sum score
    sorted_groups = [nums[idx:] for idx in range(len(nums)) if digit_sums[idx] == digit_sums[idx-1]]

    # Sort each group separately according to the index within the original list
    sorted_groups = [sorted(group, key=lambda x: (x[0], x[1])) for group in sorted_groups]

    # Flatten the list of groups and return the result
    return [num for sublist in sorted_groups for num in sublist]