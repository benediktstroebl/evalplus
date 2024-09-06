def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Amount to shift right.
    
    Returns:
    str: Resultant integer as a string after shifting.
    """
    original_x = str(x)
    shifted = original_x[shift:] + original_x[:shift]
    return shifted if len(original_x) >= shift else shifted[::-1]