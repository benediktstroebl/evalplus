def closest_integer(s):
    '''
    Rounds the given number to the closest integer, rounding away from zero.

    Args:
        s (str): Number in string form.

    Returns:
        int: The closest integer to the number.
    '''
    n = float(s)
    return round(n)