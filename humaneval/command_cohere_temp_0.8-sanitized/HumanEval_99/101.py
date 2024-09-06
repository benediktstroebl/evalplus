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
    # Check if n is equidistant from two integers and round away from zero
    if n - i == 0.5:
        return int(n - 0.5)
    return i