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

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Tiebreaker: sort by original index if digit sums are equal
    sorted_nums = sorted(zip(nums, digit_sums), key=lambda x: [x[1], x[0][0]])

    # Extract the sorted numbers and remove the digit sums (since we're done with them)
    return [n for n, _ in sorted_nums]