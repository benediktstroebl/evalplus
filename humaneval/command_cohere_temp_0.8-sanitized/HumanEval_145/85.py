def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Convert the list to a list of strings to be able to manipulate the digits.
    num_strings = [str(n) for n in nums]
    
    # Remove any leading zeros, as they don't contribute to the sorting.
    # Also, convert all strings to lowercase to ensure consistency.
    trimmed_num_strings = [num_string.lstrip('0').lower() for num_string in num_strings]

    # Calculate the total digit sums for each number.
    digit_sums = [sum(int(digit) for digit in num_string if digit != '0') for num_string in trimmed_num_strings]

    # Finally, sort the list based on the digit sums and the original index.
    sorted_idx = sorted(range(len(nums)), key=lambda i: (digit_sums[i], i))
    return [nums[idx] for idx in sorted_idx]