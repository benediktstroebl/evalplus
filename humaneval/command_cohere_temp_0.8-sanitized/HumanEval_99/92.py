def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    integer_part = int(n)
    fractional_part = n - integer_part

    if fractional_part == 0:
        return integer_part
    elif fractional_part > 0:
        return integer_part + 1
    else:
        return integer_part - 1