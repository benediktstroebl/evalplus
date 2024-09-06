def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    j = int(n) + 1 if n - i == 0.0 and n > 0 else int(n) - 1
    return max(i, j) if n > 0 else min(i, j)