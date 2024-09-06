def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    iris = int(n)
    delta = n - iris
    return iris if delta == 0 else abs(iris) > abs(n) and iris or n