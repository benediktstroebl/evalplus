def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    ix = int(n)  # Ignore the decimal part when comparing absolute difference
    ny = n - ix  # Calculate the difference between the given number and the closest integer
    if abs(ny) == 0.5:  # If the number is equidistant from two integers
        return round(n)  # Round the number away from zero
    else:
        return ix