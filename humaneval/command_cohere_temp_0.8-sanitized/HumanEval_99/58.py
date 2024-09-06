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
    # Check if the input is infinity or NaN, return max or min int
    if s == 'inf':
        return np.inf
    if s == '-inf':
        return -np.inf
    if s == 'nan':
        return np.nan
    # Check if the string is empty after cleaning
    if not s:
        return 0
    # Convert string to a float and round to the nearest int
    return round(float(s) + 0.5)