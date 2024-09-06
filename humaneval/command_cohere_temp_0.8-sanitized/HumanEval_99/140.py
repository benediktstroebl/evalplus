def closest_integer(s):
    '''
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    '''
    n = float(s)
    return round(n)