def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    
    Args:
        s (str): Numeric string value to get the closest integer for.
        
    Returns:
        int: The closest integer to the given value.
    '''
    # remove trailing '.0' if present
    s = s.rstrip('0')
    
    # check if s is already an integer
    if s.isdigit():
        return int(s)
        
    # check if s is a non-integer numeric string
    if '.' in s:
        # handle NaN (should return 0)
        if s == 'NaN': return 0
        
        # handle infinity (should return 0 respectively infinity)
        if s == 'inf': return 0
        if s == '-inf': return 0
        if s == 'infinity': return 0
        if s == '-infinity': return 0
        
        # handle non-integer values
        s = float(s)
        return round(s)
    
    # not a numeric string
    return int(s)