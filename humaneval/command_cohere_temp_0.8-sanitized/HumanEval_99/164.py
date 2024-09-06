def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    
    Args:
        s (str): Numeric string to be converted to an integer.
        
    Returns:
        int: The closest integer to the input.
    '''
    # parse the string as a float, remove the decimal part, then cast to int
    return int(round(float(s), 0))