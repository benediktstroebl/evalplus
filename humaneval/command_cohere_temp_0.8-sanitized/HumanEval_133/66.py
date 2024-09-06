def sum_squares(lst):
    """
    Return the sum of squared integers in the list, with each list item rounded up to the nearest integer.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of squared integers in the list.
    """
    # Round each element to the nearest higher integer
    rounded_lst = [math.ceil(x) for x in lst]
    # Calculate the sum of squares of the rounded values
    squared_sum = sum(x ** 2 for x in rounded_lst)
    return squared_sum