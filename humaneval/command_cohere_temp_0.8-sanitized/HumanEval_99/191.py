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
    nei = n - i
    if nei == 0.0 or nei == nei:
        return i
    elif nei > 0:
        return i + 1
    else:
        return i - 1