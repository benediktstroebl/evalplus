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
    delta = 1.0

    if n - i == 0:
        return i

    if n > i:
        delta = -1.0
        i += 1
    elif n < i:
        i -= 1

    return int(i / delta)