def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    iris = int(n)
    delta = n - iris
    return iris if delta == 0 else abs(iris) > abs(int(n)) and int(n) or iris