def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    zeros = [x for x in range(0, abs(n)) if n == x or n == -x]
    if len(zeros) == 1:
        return zeros[0]
    return zeros[1] if n > 0 else zeros[0]