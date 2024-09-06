def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the input number.
    """
    # Remove trailing fractional part and convert to float
    diff = s.rstrip('0123456789.')
    num = float(diff) if diff != '' else 0.0

    # Use the round function with a fractional value of 2 to round to the nearest even number
    # This will round away from zero for equidistant numbers
    return round(num, 2)