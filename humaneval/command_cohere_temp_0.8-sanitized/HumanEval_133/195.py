def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    for num in lst:
        if isinstance(num, float):
            num = int(num)
        result += num ** 2
    
    return int(result)