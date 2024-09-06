def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    return round(float(s), 0, abs(0-float(s)))