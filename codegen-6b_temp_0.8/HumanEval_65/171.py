
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digit_repr = str(x)
    length = len(digit_repr)
    if shift > length:
        return digit_repr[length - shift:length] + digit_repr[0:length-shift]
    else:
        return digit_repr[shift:length] + digit_repr[0:shift]
    