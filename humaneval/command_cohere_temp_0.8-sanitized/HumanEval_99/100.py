def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the input number.
    """
    # Remove trailing decimal zeros and non-numeric characters
    s = re.sub(r'[^0-9\.-]', '', s)
    
    if not s:
        return 0
    
    # Check for infinity
    if s == 'Infinity':
        return float('inf')
    if s == '-Infinity':
        return float('-inf')
    
    # Convert string to float and round to the nearest int
    # Using rounding away from zero (ROUND_HALF_UP)
    return round(float(s), 0, ROUND_HALF_UP)