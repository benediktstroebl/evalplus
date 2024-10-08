def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    assert isinstance(x, int) and isinstance(shift, int)
    digits = str(x)
    if len(digits) < shift:
        return digits[::-1]
    return digits[shift:] + digits[:shift]