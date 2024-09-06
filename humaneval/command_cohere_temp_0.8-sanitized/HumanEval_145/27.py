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

    # Convert the list to a list of strings to be able to iterate by digits
    num_strings = [str(num) for num in nums]

    # Sort the list of numbers based on the sum of digits and original index
    sorted_nums = sorted(num_strings, key=lambda x: (sum(map(int, x)), x))

    # Convert the sorted list of strings back to an list of integers
    return [int(i) for i in sorted_nums]