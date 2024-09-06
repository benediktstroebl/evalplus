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
    if delta == 0:
        return i
    elif delta > 0:
        return n // 1 if n % 1 == 0 else n // 2 * 2
    else:
        return n // -1 if n % 1 == 0 else n // -2 * -2