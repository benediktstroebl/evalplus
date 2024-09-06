def closest_integer(s):
    '''
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    '''
    n = float(s)
    diff_from_zero = abs(n) - abs(round(n))
    if diff_from_zero == 0.5:
        return round(n)
    elif diff_from_zero > 0.5:
        return round(n)
    else:
        return round(n) - 1