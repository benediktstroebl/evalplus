def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Track the sorted elements with the tiebreaker based on index.
    sorted_with_tiebreaker = []

    # Loop through each number in the input list.
    for idx, num in enumerate(nums):
        # Calculate the sum of digits for the current number.
        digit_sum = sum(map(int, str(num)))

        # Push the number and its digit sum into a tuple,
        # along with the index as a tiebreaker.
        sorted_with_tiebreaker.append((digit_sum, idx, num))

    # Sort the tuple list based on the first element of each tuple.
    sorted_result = sorted(sorted_with_tiebreaker, key=lambda x: x[0])

    # Cast the sorted result back to a list and return it.
    return [el[2] for el in sorted_result]