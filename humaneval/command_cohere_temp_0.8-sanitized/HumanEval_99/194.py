def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    negin = 1 if n > 0 else -1
    return round(n / 1) * negin