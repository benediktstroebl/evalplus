def closest_integer(s):
    """
    Return the closest integer to the given numeric string.
    
    Round away from zero if tied.
    """
    n = float(s)
    return round(n)