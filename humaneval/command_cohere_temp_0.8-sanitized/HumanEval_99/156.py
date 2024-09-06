def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the input number.
    """
    n = float(s)
    closeness = 10**10  # Largest conceivable proximity
    rounded = round(n)
    return -rounded if n < 0 else rounded if abs(n - rounded) < closeness else -rounded