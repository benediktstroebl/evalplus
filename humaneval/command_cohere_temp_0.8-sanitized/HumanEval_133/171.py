def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: The sum of squared integers in the list.
    """
    result = 0
    for n in lst:
        if isinstance(n, float):
            n = round(n)
        result += n ** 2
    
    return result