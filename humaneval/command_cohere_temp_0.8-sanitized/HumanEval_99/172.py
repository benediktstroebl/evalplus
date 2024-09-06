def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.
    
    Args:
        s (str): Numeric string representing a number.
    
    Returns:
        int: The closest integer to the given number.
    """
    n = float(s)  # Convert string to float to handle decimal values
    # Check if the number is equidistant from two integers and round away from zero
    if n % 1 == 0.5:
        return round(n)
    return int(n)