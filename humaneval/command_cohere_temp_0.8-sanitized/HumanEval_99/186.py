def closest_integer(s):
    '''
    Rounds the given number to the closest integer, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given number.
    '''
    n = float(s)
    return round(n)