def closest_integer(s):
    '''
    Rounds the given string representation of a number to the closest
    integer, rounding away from zero if equidistant.

    Args:
        s (str): String representation of a number.

    Returns:
        int: The closest integer to the given number.
    '''
    n = float(s)
    return round(n)