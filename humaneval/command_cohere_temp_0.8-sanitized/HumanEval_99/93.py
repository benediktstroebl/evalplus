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
    d = n - i
    if d == 0:
        return i
    elif d > 0:
        return i + 1
    else:
        return i - 1