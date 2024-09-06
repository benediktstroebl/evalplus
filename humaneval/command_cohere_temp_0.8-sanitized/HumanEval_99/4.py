def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    d = abs(n)
    return round(n) if d == 0 or n % 1 == 0 else round(n, away_from=0)