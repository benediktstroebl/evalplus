def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    ii = int(n)
    if n - ii == 0:
        return ii
    elif n > ii:
        return ii + 1
    else:
        return ii - 1