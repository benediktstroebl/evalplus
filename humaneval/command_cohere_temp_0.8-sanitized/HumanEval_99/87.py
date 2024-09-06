def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    idx = n % 1
    if idx == 0:
        return int(n)
    elif idx < 0:
        return int(n - idx)
    else:
        return int(n + idx)