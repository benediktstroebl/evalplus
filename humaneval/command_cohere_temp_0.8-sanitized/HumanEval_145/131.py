def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # Ensure the list is not empty
    if not nums:
        return []

    # Initialize a list to store the sorted integers
    sorted_nums = []

    # Iterate through the original list of integers
    for num in nums:
        # Initialize a variable to store the current digit sum
        digit_sum = 0

        # Iterate through the digits of the integer
        for digit in str(num):
            # Add the digit to the running total of digit sums
            digit_sum += int(digit)

        # Append the original integer and its digit sum to the sorted list
        sorted_nums.append((num, digit_sum, num))

    # Sort the list of tuples in ascending order of the second element (digit sum)
    sorted_nums.sort(key=lambda x: x[1])

    # Reconstruct the original list of integers, ordering ties by the third element (original value)
    return [num for num, digit_sum, _ in sorted_nums]