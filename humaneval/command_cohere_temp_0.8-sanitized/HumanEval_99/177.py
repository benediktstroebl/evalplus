def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    val, inv = n, 1.0 - (n / 10) if n % 10 == 0.0 else n % 10
    return round(val if val >= 0.0 else inv)