def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    near_zero = abs(n - i) < 1e-5 and n > 0 and n < 1
    return i if near_zero else n if n % 1 == 0 else n + np.sign(n)