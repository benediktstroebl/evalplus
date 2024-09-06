def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    delta = abs(n - i)
    if delta < 1e-5:  # Check for equidistance
        return i if n >= 0 else -i  # Round away from zero
    return round(n)