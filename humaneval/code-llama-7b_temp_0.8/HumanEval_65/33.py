
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = ''
    digits = str(x)
    shift_for_digits = len(digits) - shift
    if shift > len(digits):
        return digits[::-1]
    return digits[shift_for_digits:] + digits[:shift_for_digits]

