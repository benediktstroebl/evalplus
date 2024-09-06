def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    ix = int(n)  # Attempt to cast n as an integer.
    if n == ix:
        return ix
    return round(n, 0, -1)