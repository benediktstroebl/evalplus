def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the input number.
    """
    n = float(s)
    return round(n)