def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    
    # Square each element and round it up to the nearest integer
    squared = [int(x**2) for x in lst if x >= 1]
    
    return sum(squared)