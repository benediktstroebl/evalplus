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
    
    # Convert the list to a list of strings for summing digits.
    num_strings = [str(n) for n in nums]
    
    # Calculate the sum of digits for each number and sort by this criterion.
    digit_sums = [sum(int(d) for d in num_string) for num_string in num_strings]
    sorted_indices = sorted(range(len(digit_sums)), key=lambda i: digit_sums[i], reverse=False)
    
    # Reconstruct the sorted list based on the sorted indices.
    sorted_list = [nums[i] for i in sorted_indices]
    
    return sorted_list