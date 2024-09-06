def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift
    shift (int): Amount to shift by
    
    Returns:
    str: String of the shifted integer
    """
    assert isinstance(x, int) and isinstance(shift, int)
    num_digits = len(str(x))
    if shift > num_digits:
        shift = num_digits
    shifted = str(x)
    end = num_digits - shift
    return shifted[-end:]+shifted[:-end]