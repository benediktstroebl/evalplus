def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string value to convert to an integer.

    Returns:
        int: The closest integer to the input.
    """
    # Remove trailing decimal zeros and non-numeric characters
    s = re.sub(r'[^\d.]', '', s)
    # Check if the input is already an integer (without decimal part)
    if s == str(round(float(s), 0)):
        return int(s)
    # Check if the input is zero to optimize the case
    if s == '0':
        return 0
    # Convert to float and round using the correct rounding rule
    return round(float(s), 0, rounding=math.ceil)