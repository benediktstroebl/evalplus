def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.
    
    Args:
        s (str): Numeric string representation of a number.
    
    Returns:
        int: The closest integer to the given number.
    """
    n = float(s)
    return round(n)