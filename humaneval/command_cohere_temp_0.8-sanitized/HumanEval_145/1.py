def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    # Empty list handling
    if not nums:
        return []

    # Creating a dictionary to store the sum of digits and index for each number
    num_dict = {}
    for idx, num in enumerate(nums):
        dig_sum = sum(map(int, str(num)))
        if dig_sum in num_dict:
            num_dict[dig_sum].append(idx)
        else:
            num_dict[dig_sum] = [idx]

    # Sorting the numbers based on the sum of digits in case of tie, use the index as a tiebreaker