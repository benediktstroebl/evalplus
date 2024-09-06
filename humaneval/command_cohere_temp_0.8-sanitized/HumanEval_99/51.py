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
    if delta < 1e-5:  # Cover the case of -0.0
        return i if n >= 0 else -i
    else:
        return n // 1 if n % 1 == 0 else n // 1 + 1 if n > 0 else n // 1 - 1