def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: Sum of squared integers.
    """
    result = 0
    for n in lst:
        if isinstance(n, int): 
            result += n ** 2 
    return result