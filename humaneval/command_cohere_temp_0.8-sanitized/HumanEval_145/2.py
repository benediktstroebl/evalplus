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

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(num)) for num in nums]
    sorted_digits = sorted(zip(digit_sums, nums), key=lambda x: (x[0], x[1][0]))

    # Extract the sorted numbers and return.
    return [num for digit_sum, num in sorted_digits]