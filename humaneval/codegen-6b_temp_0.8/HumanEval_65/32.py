
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert shift >= 0
    str_len = len(str(x))
    digits = str(x)
    first_digit = digits[0]
    if shift > str_len:
        shift -= str_len
        digits = digits[::-1]
    shifted_chars = digits[shift:] + digits[:shift]
    return shifted_chars

