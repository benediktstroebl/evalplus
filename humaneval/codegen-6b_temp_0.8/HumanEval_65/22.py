
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    r = str(x)
    if shift > len(r):
        r = r[::-1]
        return r[:len(r) - shift] + r[len(r) - shift:]
    else:
        return r[len(r) - shift:] + r[:len(r) - shift]
