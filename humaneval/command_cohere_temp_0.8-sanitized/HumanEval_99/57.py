def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    idx = n % 1 if n % 1 != 0 else 0
    return round(n) if idx > 0 else -round(-n)