def closest_integer(s):
    '''
    Rounds the given number to the closest integer, rounding away from zero.

    Args:
        s (str): Number in string format.

    Returns:
        int: The closest integer to the given number.
    '''
    n = float(s)
    return round(n)