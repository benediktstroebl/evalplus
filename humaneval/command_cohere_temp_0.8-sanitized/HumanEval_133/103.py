def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    # Iterate through the list and square each number
    for num in lst:
        result += num ** 2
    
    # Return the value rounded up to the nearest integer
    return int(result)