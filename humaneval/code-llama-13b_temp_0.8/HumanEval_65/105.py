
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # 1234
    # 4123
    # 3412
    # 2341
    # 1234
    digits = list(str(x))
    shift = shift % len(digits)
    shifted = digits[shift:] + digits[:shift]
    return "".join(shifted)

