def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the given number.
    """
    n = float(s)  # Convert string to float to handle decimal values
    return round(n) if n % 1 else int(n)