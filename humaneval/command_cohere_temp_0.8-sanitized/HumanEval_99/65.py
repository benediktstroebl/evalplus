def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    
    Args:
        s (str): Numeric string value to convert to an integer.
    
    Returns:
        int: The closest integer to the input.
    '''
    return round(float(s), 0, -1)