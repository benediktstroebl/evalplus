def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    i = int(n)
    delta = 1.0 / n
    return i - (delta // 2.0) if delta % 1.0 == 0 else i