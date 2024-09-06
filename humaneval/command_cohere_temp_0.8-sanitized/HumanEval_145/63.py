def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Calculate the sum of digits for each number
    digit_sums = [sum(int(d) for d in str(num)) for num in nums]

    # Sort by digit sums with tiebreak by index
    sorted_nums = sorted(zip(nums, digit_sums), key=lambda x: (x[1], x[0][0]))

    # Unzip the sorted list and digit sums
    return [num for num, _ in sorted_nums]