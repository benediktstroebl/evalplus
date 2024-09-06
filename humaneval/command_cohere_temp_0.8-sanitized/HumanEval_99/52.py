def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    delta = abs(n - i)
    if delta < 1e-6:
        return i
    elif n > i:
        return i + 1
    else:
        return i - 1