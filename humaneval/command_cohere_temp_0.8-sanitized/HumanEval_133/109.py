def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the next integer.
    """
    result = 0
    for n in lst:
        result += n**2

    return int(result)**0.5