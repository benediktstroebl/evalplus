def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: Sum of squared integers rounded up to the next integer.
    """
    result = sum(int(round(n)**2 for n in lst if n >= 0))
    return result