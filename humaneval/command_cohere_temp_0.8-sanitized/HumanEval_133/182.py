def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    # Loop through each element in the list and round up to the nearest integer
    for num in lst:
        result += int(num**2)**(0.5)
    return result