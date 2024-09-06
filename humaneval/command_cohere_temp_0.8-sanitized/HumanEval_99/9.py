def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string to be converted to an integer.

    Returns:
        int: The closest integer to the input.
    """
    # Ensure the decimal point is always to the right of the precision of a 4-byte float
    n = round(float(s), 0, -float('inf'))
    if n % 1 == 0:
        return int(n)
    else:
        return int(n) + 1 if n > 0 else int(n) - 1