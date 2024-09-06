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
    closer_to_zero = abs(n - i) == 0.5
    return i if closer_to_zero else -i if n > 0 else i