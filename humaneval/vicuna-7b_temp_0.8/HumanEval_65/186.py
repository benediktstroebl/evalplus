
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    return "".join(map(str, (x // (shift % len(str(x))) + (shift % len(str(x)))) if not isinstance(x, basestring) else map(str, x)[:shift % len(str(x))]) if isinstance(x, int) else x for x in (x, shift))
