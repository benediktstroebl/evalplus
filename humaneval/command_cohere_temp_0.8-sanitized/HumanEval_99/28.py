def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    i = int(n)
    delta = abs(n - i)
    if delta < 1e-5:  # Close enough to an integer
        return i
    elif n > 0:
        return i + (n - i) // 2
    else:
        return i - (i - n) // 2