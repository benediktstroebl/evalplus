def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    for n in lst:
        rounded_n = int(n**2)**0.5
        result += rounded_n
    return result