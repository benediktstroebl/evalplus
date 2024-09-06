def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Amount to shift right.
    
    Returns:
    str: Resultant string after shifting.
    """
    digits = str(x)
    if len(digits) < shift:
        return digits[len(digits) % shift:] + digits[:len(digits) % shift]
    return digits[-shift:] + digits[:-shift]