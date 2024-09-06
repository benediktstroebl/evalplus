def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    # Ensure the list is not empty
    if not nums:
        return []

    # Convert the list to a list of strings to be able to extract digits
    num_strings = [str(num) for num in nums]

    # Extract the digit sums and sort the numbers accordingly
    digit_sums = [sum(int(d) for d in num_string if d.isdigit()) for num_string in num_strings]
    sorted_indices = sorted(range(len(digit_sums)), key=lambda i: digit_sums[i])

    # Retrieve the original numbers sorted by digit sum and tiebreaker index
    sorted_nums = [nums[idx] for idx in sorted_indices]
    return sorted_nums