def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to criteria above.
    """
    if len(nums) == 0:
        return []

    # Calculate the sum of digits for each number in the list.
    total_digits = [sum(map(int, str(n))) for n in nums]

    # Tiebreak decisions are made in case of identical digit sums:
    sorted_nums = sorted(zip(nums, total_digits), key=lambda x: (x[1], x[0][0]))

    # List of integers after sorting by digit sum.
    sorted_by_digit_sum = [num for digit_sum, num in sorted_nums]

    # Finally, the list is sorted in increasing order of digit sum,
    # with tiebreak decisions based on the index of the integer in the original list.
    return sorted_by_digit_sum