def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = sum(int(round(n)**2 for n in lst if n != 0 and isinstance(n, (int, float))))
    return result