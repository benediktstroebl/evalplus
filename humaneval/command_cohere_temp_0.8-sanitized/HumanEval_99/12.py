def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string to be converted to an integer.

    Returns:
        int: The closest integer to the input.
    """
    # Ensure the number is expressed in decimal points and remove trailing zeros
    num = str(float(s.rstrip('0'))).rstrip('.')
    if num[0] == '-':
        return int(num + '0' if num[-1] == '.' else '.0')
    return int(num + '0' if num[-1] == '.' else '.0')