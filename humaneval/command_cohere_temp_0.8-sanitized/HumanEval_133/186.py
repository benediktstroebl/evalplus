def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: The sum of squared integers.
    """
    result = 0
    for num in lst:
        num = int(num) ** 2
        result += num
    
    return result