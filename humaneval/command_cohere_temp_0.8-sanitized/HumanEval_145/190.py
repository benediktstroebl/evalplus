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

    # Convert the list to strings for easier manipulation
    num_strings = [str(num) for num in nums]

    # Calculate the sum of digits for each number and sort by this value
    sorted_by_sum = sorted(num_strings, key=lambda x: sum(char.isdigit() and int(char) or 0 for char in x))

    # Extract the original list elements using the sorted strings
    sorted_nums = [int(str_num) for str_num in sorted_by_sum]

    # Further sort in the case of ties, using the index in the original list
    sorted_nums.sort(key=lambda num: (num, nums.index(num)))

    return sorted_nums