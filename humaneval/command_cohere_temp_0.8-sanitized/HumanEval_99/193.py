def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    near_zero = abs(n - i) < 1e-5 and n > 0 or abs(n - i) < 1e-5 and n < 0  # Check for equidistance from zero
    if near_zero:
        return i + 1 if n > 0 else i - 1
    return int(n)