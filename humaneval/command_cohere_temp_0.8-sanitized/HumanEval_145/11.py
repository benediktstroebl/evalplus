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

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # List of tuples: sort key is the sum-of-digits score, tiebreak is the index in the original list
    sorted_nums = sorted(zip(digit_sums, nums), key=lambda x: x[0], reverse=False)

    # Extract the sorted integers list
    return [n for _, n in sorted_nums]