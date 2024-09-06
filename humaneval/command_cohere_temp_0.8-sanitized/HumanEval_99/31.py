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
    delta = abs(n - i)
    if delta < 1e-5:  # Cover the case when float is effectively integer
        return i
    elif n > 0:
        return i + 1 if delta == 0.5 else i
    else:
        return i - 1 if delta == 0.5 else i