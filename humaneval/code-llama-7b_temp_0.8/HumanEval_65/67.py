
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = "0123456789"
    new_shift = shift % len(str(x))
    new_digits = list(str(x))
    new_digits = new_digits[-new_shift:] + new_digits[:-new_shift]
    return "".join(new_digits)

