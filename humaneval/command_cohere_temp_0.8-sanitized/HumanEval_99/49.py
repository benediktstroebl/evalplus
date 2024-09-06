def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    ix = int(n)  # Attempt to convert to integer,
    # and if it fails, float(n) is n (no exception raised)
    return round(n - (ix if ix == n else 0), 0) + (ix if ix == n else 0)