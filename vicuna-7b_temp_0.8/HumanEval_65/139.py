
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # handle special case of negative shift
    if shift < 0:
        shift += len(str(x)) * abs(shift)
    # handle special case of zero shift
    if not shift:
        return x
    # handle special case of positive shift one digit
    if len(str(x)) - shift < len(str(x)):
        return "0" + x[-shift:]
    # handle general case of positive shift multiple digits
    while shift >= len(str(x)):
        x = "0" + x[:-1]
        shift -= len(str(x))
    return str(x) + "0"[:-shift]