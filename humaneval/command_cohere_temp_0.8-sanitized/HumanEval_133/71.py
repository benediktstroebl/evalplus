def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: The sum of squared integers.
    """
    result = 0
    for n in lst:
        rounded_n = int(n)
        result += rounded_n ** 2
    return result