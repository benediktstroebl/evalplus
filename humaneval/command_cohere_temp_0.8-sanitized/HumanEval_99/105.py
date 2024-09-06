def closest_integer(s):
    '''
    Rounds the given string representation of a number to the closest
    integer, rounding away from zero if equidistant.

    Args:
        s (str): Number string to be rounded.

    Returns:
        int: The closest integer to the input number.
    '''
    n = float(s)
    return round(n)