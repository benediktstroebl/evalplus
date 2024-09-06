
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = str(x)
    # If shift > number of digits, return digits reversed.
    if len(digits) < abs(shift):
        return str(x)[::-1]
    if shift > 0:
        return digits[shift:] + digits[0:shift]
    else:
        return digits[-shift:] + digits[0:-shift]

