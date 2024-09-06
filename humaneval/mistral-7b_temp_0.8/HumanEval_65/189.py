
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digit_count = len(str(x))
    if shift > digit_count:
        return str(x)[::-1]
    else:
        shifted = str(x)[shift:] + str(x)[:shift]
        return shifted
