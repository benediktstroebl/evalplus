def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list of integers.
    """
    if not nums:
        return []

    # Find the digits sum for each number in the list.
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by sum of digits (with Ties resolved by index in original list)
    # Use the tuple sorting key `lambda x: (x[0], -x[1])`
    sorted_nums = sorted(zip(digit_sums, nums), key=lambda x: (x[0], -x[1]))

    # Extract the sorted list of integers from the sorted list of tuples.
    sorted_nums = [i[1] for i in sorted_nums]

    return sorted_nums