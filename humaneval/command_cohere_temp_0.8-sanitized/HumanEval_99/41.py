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
    if delta < 1e-5:  # Cover the case where the float is effectively an integer
        return i
    elif n > 0:
        return i + 1 if delta == 0.5 else i
    else:
        return i - 1 if delta == 0.5 else i