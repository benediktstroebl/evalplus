def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Convert the list to a list of strings to be able to manipulate the digits.
    num_strings = [str(num) for num in nums]

    # Reverse the sorting order of the sum of the digits.
    # This is done by summing the index of the digit instead of the digit itself.
    # E.g. '2' -> 0, '12' -> 1, '123' -> 2, ...
    digit_indices = [sum(map(int, str(num))) for num in num_strings]

    # Finally, sort the numbers according to the digit sums with tiebreaks.
    # Note the reversed(), since we want ascending order.
    return sorted(nums, key=lambda num: (digit_indices.index(sum(map(int, str(num)))), num), reverse=True)