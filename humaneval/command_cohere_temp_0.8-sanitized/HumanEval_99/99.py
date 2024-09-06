def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the input number.
    """
    # Remove trailing zeros and decimal points
    s = re.sub(r'[.\d]*0$', '', s)
    # Allow explicit rounding
    if s.endswith('Infinity'):
        return int(s[:-9])
    # Check for invalid strings
    if not s.isdigit():
        raise ValueError('Invalid input: {} is not a number.'.format(s))
    # Convert string to a float and round to the closest int
    return round(float(s), 0, -1)