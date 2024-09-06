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

    # Reverse the sorting order to get the largest digit sum at the beginning.
    # The list is sorted by digit sum with tiebreaks decided by the index.
    sorted_digits = sorted(enumerate(num_strings), key=lambda x: (len(x[1]), x[0]))

    # Create a new list with the sorted integers.
    sorted_nums = [int(digit) for idx, digit in sorted_digits]
    return sorted_nums