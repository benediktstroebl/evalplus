def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    neginf = 1e10
    posinf = -1e10
    if n == neginf or n == posinf:
        return int(n)
    elif n % 1 == 0:
        return int(n)
    elif n > 0:
        return int(n + 0.5)
    else:
        return int(n - 0.5)