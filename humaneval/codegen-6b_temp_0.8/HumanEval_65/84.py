
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x, shift = int(x), int(shift)
    digits = len(str(x))
    if shift > digits:
        return str(x)[::-1]
    return str(x)[digits-shift:shift+digits] + str(x)[:digits-shift]

