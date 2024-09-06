def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    integer_val = round(n)
    if integer_val == int(integer_val):
        return int(integer_val)
    elif n > 0:
        return int(integer_val + 1)
    else:
        return int(integer_val - 1)