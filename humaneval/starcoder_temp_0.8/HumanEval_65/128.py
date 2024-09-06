
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if not isinstance(x, int):
        raise TypeError("Argument must be an integer")
    if x < 0:
        raise ValueError("Argument must be positive")
    if x < 10:
        return str(x)
    digits = list(str(x))
    if shift > len(digits):
        shift = shift % len(digits)
        return "".join(digits[shift:] + digits[:shift])
    return "".join(digits[shift:] + digits[:shift])

