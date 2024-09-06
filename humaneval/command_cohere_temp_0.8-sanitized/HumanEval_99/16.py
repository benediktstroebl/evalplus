def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string value to convert to an integer.

    Returns:
        int: The closest integer to the input.
    """
    # Remove trailing fractional part and convert to float
    val = float(s.rstrip('0123456789'))
    # Determine the closest integer and correct rounding direction
    return round(val, 0, -1 if val > 0 else 1)