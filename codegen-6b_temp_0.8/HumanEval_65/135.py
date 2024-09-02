
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Represent all numbers in list form
    digits = list(str(x))
    # Shift by the shift value
    shifted = digits[shift:] + digits[:shift]
    return ''.join(shifted)

