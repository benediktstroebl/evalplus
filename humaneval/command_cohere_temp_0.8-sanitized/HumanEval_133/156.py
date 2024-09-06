def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next bigger integer.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of squared integers in the list.
    """

    # Handle the edge case where the list is empty
    if not lst:
        return 0

    # Use a list comprehension to square each element and round up
    rounded_lst = [math.ceil(x * x) for x in lst]

    # Calculate the sum of the squared integers
    result = sum(rounded_lst)
    return result