def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    io = int(n)
    if n - io == 0:
        return io
    elif n > io:
        return io + 1
    else:
        return io - 1