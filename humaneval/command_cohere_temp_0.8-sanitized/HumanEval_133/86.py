def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers in the list.
    """
    result = 0
    for n in lst:
        result += int(n**2 if n % 1 == 0 else n)
    return result