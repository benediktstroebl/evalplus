def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    # Check if the number is equidistant from two integers
    # and round it away from zero
    if n % 1 == 0.5:
        return round(n)
    return int(n)