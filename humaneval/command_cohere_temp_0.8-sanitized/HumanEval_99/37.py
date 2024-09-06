def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string to be converted to an integer.

    Returns:
        int: The closest integer to the input.
    """
    # Remove trailing fractional part
    i = s.rfind(".")
    if i != -1:
        s = s[:i]
    # Handle negative cases and convert to int
    num = int(s)
    if num < 0:
        return -((-num) // 2) * 2
    return ((num + 1) // 2) * 2