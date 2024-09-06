def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    
    Args:
        s (str): Numeric string representation

    Returns:
        int: The closest integer to the given numeric string
    '''
    # remove trailing .0 to avoid rounding issues
    # e.g. '14.50' -> '14.5'
    s = s.rstrip('0')
    
    # check for cases where the number is actually an integer
    if s == s.rstrip('.'):
        return int(s)

    # check if the string is beyond the decimal range of ints
    # e.g. '3.14e100' -> '3e100'
    if 'e' in s:
        s = s.replace('e', 'e+')
        if int(s[:-1]) % 10 == 0:
            return int(s[:-1])

    # convert to float and get the closest int
    return round(float(s), 0, rounding='away')