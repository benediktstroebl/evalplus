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
    # Check if n is equidistant from integers and round away from zero
    if n - i == 0.5:
        return i if i >= 0 else -i
    return int(n)