def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    iris = [floor(n), ceil(n)]
    if iris[0] == iris[1]:
        return iris[1]
    else:
        return iris[0]